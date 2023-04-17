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

class SolutionFileSchema(BaseModel):
    filename: str
    type: str
    content: str
    clean_db: bool = False
    encapsulate_in_fn: bool = False
    avoid_main: bool = False


class ChallengeSchema(BaseModel):
    name: str
    solution: List[SolutionFileSchema]
    tests: List[FileSchema]


class SubmissionSchema(BaseModel):
    user_id: int
    files: List[FileSchema]


class ChallengeController:

    def __init__(self):
        self.pyworker = Pyworker()

    async def get_all(self):
        challenges = Challenge.objects.all()
        return [challenge.to_mongo() for challenge in challenges]


    async def get(self, challenge_id):
        challenge = Challenge.objects.get(_id=challenge_id)
        return challenge.to_mongo()


    async def create(self, data: ChallengeSchema):
        solutions = [solution.dict() for solution in data.solution]
        tests = [test.dict() for test in data.tests]

        """
        TODO: Validar la solucion y los tests enviandolo al worker para que se
        ejecuten. En caso de no ser exitoso, se debe lanzar una excepción (RequestException)
        """

        challenge = Challenge(name=data.name, solution=solutions, tests=tests)
        return challenge.save().to_mongo()


    async def update(self, challenge_id, data: ChallengeSchema):
        challenge = Challenge.objects.get(_id=challenge_id)
        challenge.update(name=data.name, solution=data.solution, tests=data.tests)
        return challenge.to_mongo()


    async def delete(self, challenge_id):
        challenge = Challenge.objects.get(_id=challenge_id)
        return challenge.delete().to_mongo()


    async def submit(self, challenge_id, user_id, solution: SubmissionSchema):
        challenge = Challenge.objects.get(_id=challenge_id)
        
        solution_files = [File(**dict(file)).to_mongo() for file in solution.files]
        challenge.solution = solution_files

        """
        TODO: Validar la solución enviando el challenge al worker.
        Si el resultado no es exitoso, arrojar una excepción (InvalidSolutionException)
        """

        UserController()._add_or_replace_solution(
            user_id,
            Solution(challenge_id=challenge_id, files=solution_files, score_earned=0)) # Acá usar el score que se recibio en el response

        """
        TODO: Retornar resultados de ejecución de la solución. (Response)
        """
        return {}

    def _map_challenge_to_worker(self, challenge):
        return {
            "files": challenge.solution,
            "tests": challenge.tests,
            "clean_db": challenge.clean_db,
            "encapsulate_in_fn": challenge.encapsulate_in_fn,
            "avoid_main": challenge.avoid_main
        }
