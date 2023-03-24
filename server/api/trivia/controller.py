#!/usr/bin/env python

import uuid
from typing import List
from pydantic import BaseModel
from .model import TriviaChallenge
from ..exceptions.RequestException import RequestException
from ..domain.clients.redis import Redis

class OptionSchema(BaseModel):
    text: str
    is_correct: bool


class TriviaChallengeSchema(BaseModel):
    name: str
    statement: str
    options: List[OptionSchema]


class TriviaChallengeController:
    def __init__(self):
        self.redis = Redis()

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
    
    
    async def create_session(self, id):
        challenge = self.get(id)
        random_id = uuid.uuid4()
        session = self.redis.set(random_id, challenge)
        if not session:
            raise RequestException("No se pudo crear la sesión", status_code=500)
        challenge.session_id = random_id
        return challenge
    