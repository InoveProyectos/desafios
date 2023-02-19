from .model import Challenge, Solution
from ..user.model import User
from pydantic import BaseModel
from typing import List

class ScriptFileSchema(BaseModel):
    filename: str
    type: str
    content: str
    clean_db: bool = False
    encapsulate_in_fn: bool = False
    avoid_main: bool = False


class TestFileSchema(BaseModel):
    filename: str
    type: str
    content: str


class ChallengeSchema(BaseModel):
    name: str
    solution: List[ScriptFileSchema]
    tests: List[TestFileSchema]


class SubmissionSchema(BaseModel):
    files: List[ScriptFileSchema]


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
        user = User.objects.get(_id=user_id)

        solution = {"challenge_id": challenge_id, "solution": solution.files}

        user.save()
        """
        Validar la solución usando el worker. 
        Agregar la solucion al user.
        Actualizar el user score y retornar el resultado.
        """

        return {}
