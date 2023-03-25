#!/usr/bin/env python

import uuid
import random
from typing import List
from pydantic import BaseModel
from .model import TriviaChallenge
from ...domain.exceptions.RequestException import RequestException
from ...domain.clients.redis import Redis

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
        trivia_challenges = TriviaChallenge.objects.all()
        return [trivia_challenge.to_mongo() for trivia_challenge in trivia_challenges]
    

    async def get(self, id):
        trivia_challenge = TriviaChallenge.objects.get(id=id)
        return trivia_challenge.to_mongo()
    

    async def create(self, trivia_challenge: TriviaChallengeSchema):
        self.validate_challenge_options(trivia_challenge.options)
        print(trivia_challenge.dict())
        trivia_challenge = TriviaChallenge(**trivia_challenge.dict()).save()
        return trivia_challenge.to_mongo()

    
    async def update(self, id, trivia_challenge: TriviaChallengeSchema):
        trivia_challenge = TriviaChallenge.objects.get(id=id)
        trivia_challenge.update(**challenge)
        return trivia_challenge.to_mongo()

    
    async def delete(self, id):
        trivia_challenge = TriviaChallenge.objects.get(id=id)
        return trivia_challenge.delete().to_mongo()
    
    
    async def create_session(self, id):
        trivia_challenge = self.get(id)
        random_id = uuid.uuid4()

        corrects = [i for i in range(len(trivia_challenge.options)) if trivia_challenge.options[i].is_correct]
        trivia_challenge.options =  self._shuffle_options(trivia_challenge.options)
        
        session = self.redis.set(random_id, corrects)
        if not session:
            raise RequestException("No se pudo crear la sesión", status_code=500)

        return trivia_challenge
    

    def _shuffle_options(self, options):
        random.shuffle(options)
        return [{"text": option["text"], "index": i} for i, option in enumerate(options, start=1)]


    def _without(self, dictionary, key):
        return {k: v for k, v in dictionary.items() if k != key}
