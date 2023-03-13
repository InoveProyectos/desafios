#!/usr/bin/env python

from .model import TriviaChallenge
from pydantic import BaseModel
from typing import List
from ..exceptions.RequestException import RequestException

class OptionSchema(BaseModel):
    text: str
    is_correct: bool


class TriviaChallengeSchema(BaseModel):
    name: str
    statement: str
    options: List[OptionSchema]


class TriviaChallengeController:

    def validate_challenge_options(self, options):
        if not any(option.is_correct for option in options):
            raise RequestException("Es necesario que exista al menos una opción correcta", status_code = 400)


    async def get_all(self):
        challenges = TriviaChallenge.objects.all()
        return [challenge.to_mongo() for challenge in challenges]
    

    async def get(self, id):
        challenge = TriviaChallenge.objects.get(id=id)
        return challenge.to_mongo()
    

    async def create(self, challenge: TriviaChallengeSchema):
        self.validate(validate_challenge_options(challenge.options))
        challenge = TriviaChallenge(**challenge).save()
        return challenge.to_mongo()

    
    async def update(self, id, challenge: TriviaChallengeSchema):
        challenge = TriviaChallenge.objects.get(id=id)
        challenge.update(**challenge)
        return challenge.to_mongo()

    
    async def delete(self, id):
        challenge = TriviaChallenge.objects.get(id=id)
        return challenge.delete().to_mongo()