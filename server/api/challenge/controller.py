from .model import Challenge, File
from ..user.model import User, Solution
from ..user.controller import UserController
from pydantic import BaseModel
from typing import List

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
    files: List[FileSchema]


class ChallengeController:

    async def get_all(self):
        challenges = Challenge.objects.all()
        return [block.to_mongo() for block in challenges]


    async def get(self, challenge_id):
        challenge = Challenge.objects.get(_id=challenge_id)
        return challenge.to_mongo()


    async def create(self, data: ChallengeSchema):
        solutions = [solution.dict() for solution in data.solution]
        tests = [test.dict() for test in data.tests]

        """
        TODO: Validar la solucion y los tests enviandolo al worker para que se
        ejecuten. En caso de no ser exitoso, se debe lanzar una excepción (InvalidChallengeException)
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
        TODO: Validar la solución enviando el challenge al worker. Calcular el score obtenido
        """
        UserController()._add_or_replace_solution(
            user_id, 
            # score_earned
            Solution(challenge_id=challenge_id, files=solution_files))

        """
        TODO: Retornar resultados de ejecución de la solución.
        """
        return {}