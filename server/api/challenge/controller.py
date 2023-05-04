#!/usr/bin/env python

from typing import List
from pydantic import BaseModel
from ...domain.services import Pyworker
from .model import Challenge, File
from ..user.model import User, Solution
from ..user.controller import UserController
from ...domain.exceptions import RequestException


class FileSchema(BaseModel):
    filename: str
    type: str
    content: str


class ChallengeSchema(BaseModel):
    name: str
    solution: List[FileSchema]
    tests: List[FileSchema]
    clean_db: bool = False
    encapsulate_in_fn: bool = False
    avoid_main: bool = False


class SubmissionSchema(BaseModel):
    user_id: int
    solution: List[FileSchema]


class ChallengeController:

    def __init__(self):
        self.pyworker = Pyworker()


    async def get_all(self):
        challenges = Challenge.objects.all()
        return [challenge.to_mongo() for challenge in challenges]


    async def get(self, id):
        challenge = Challenge.objects.get(_id=id)
        return challenge.to_mongo()


    async def create(self, data: ChallengeSchema):
        solutions = [solution.dict() for solution in data.solution]
        tests = [test.dict() for test in data.tests]

        pytest_response = self.pyworker.run_code(solutions, tests, encapsulate_in_fn = data.encapsulate_in_fn,
                                                 clean_db=data.clean_db, avoid_main=data.avoid_main)

        try:
            passed = self._passed(pytest_response.json())            
        except Exception as e:
            raise RequestException(f"Tu solución no pudo ser evaluada: {str(e)}", status_code = 400)

        if not passed:
            errors = self._search_failed_tests(pytest_response.json())
            raise RequestException("Tu solución no pasó los tests", status_code = 400, failure = errors)            

        challenge = Challenge(name=data.name, solution=solutions, tests=tests,
                              encapsulate_in_fn=data.encapsulate_in_fn, clean_db=data.clean_db, avoid_main=data.avoid_main)
        
        return challenge.save().to_mongo()


    async def update(self, id, data: ChallengeSchema):
        challenge = Challenge.objects.get(_id=id)
        challenge.update(
            name=data.name, solution=data.solution, tests=data.tests)
        return challenge.to_mongo()


    async def delete(self, id):
        challenge = Challenge.objects.get(_id=id)
        return challenge.delete().to_mongo()


    async def submit(self, id, data: SubmissionSchema):
        challenge = Challenge.objects.get(_id=id)

        solution_files = self._document_list_to_dict_list([File(**dict(file)) for file in data.solution])
        test_files = self._document_list_to_dict_list(challenge.tests)

        pytest_response = self.pyworker.run_code(solution_files, test_files, clean_db=challenge.clean_db, encapsulate_in_fn=challenge.encapsulate_in_fn, avoid_main=challenge.avoid_main)

        try:
            passed = self._passed(pytest_response.json())         
        except Exception as e:
            raise RequestException(f"Tu solución no pudo ser evaluada: {str(e)}", status_code = 400)

        score_earned = self._calculate_score(pytest_response.json())

        UserController()._add_or_replace_solution(
            data.user_id,
            Solution(challenge_id=id, files=solution_files, score_earned=score_earned))

        return dict(passed=passed, score=score_earned, results = pytest_response.json())


    def _map_challenge_to_worker(self, challenge):
        return {
            "files": challenge.solution,
            "tests": challenge.tests,
        }


    def _calculate_score(self, pytest_response):
        summary = pytest_response["summary"]
        return int(summary["passed"]) / int(summary["total"]) * 100


    def _passed(self, pytest_response):
        summary = pytest_response["summary"]
        return summary["passed"] == summary["total"]    
    

    def _search_failed_tests(self, pytest_response):
        return [result for result in pytest_response["results"] if not result["passed"]]


    def _document_list_to_dict_list(self, document_list):
        return [dict(document.to_mongo()) for document in document_list]
