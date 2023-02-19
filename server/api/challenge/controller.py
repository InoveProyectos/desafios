from .model import Challenge
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
        challenge = Challenge(name=data.name, solution=solutions, tests=tests)
        return challenge.save().to_mongo()


    async def update(self, challenge_id, data: ChallengeSchema):
        challenge = Challenge.objects.get(_id=challenge_id)
        challenge.update(name=data.name, solution=data.solution, tests=data.tests)
        return challenge.to_mongo()


    async def delete(self, challenge_id):
        challenge = Challenge.objects.get(_id=challenge_id)
        return challenge.delete().to_mongo()
