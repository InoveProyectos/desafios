#!/usr/bin/env python

import json
import random
from typing import List
from pydantic import BaseModel
from ..model import TriviaChallenge
from ....domain.exceptions.RequestException import RequestException
from ....domain.clients.redis import Redis

class AnswerSchema(BaseModel):
    id: str
    selected: List[int]

class SessionController:
    def __init__(self):
        self.redis = Redis()


    async def create(self, trivia_id=None):
        if not trivia_id:
            raise RequestException("Es necesario indicar de qué trivia querés crear una sesión, por ejemplo ?trivia_id=43", status_code=400)
        trivia_challenge = TriviaChallenge.objects.get(_id=trivia_id)
        corrects =  self._shuffle_options(trivia_challenge)
        redis_key = self._generate_redis_key()
        session = self.redis.set(redis_key, self._serialize(trivia_challenge, corrects))
        if not session:
            raise RequestException("No se pudo crear la sesión", status_code=500)
        return { "session_id": redis_key, "challenge": trivia_challenge.to_mongo() }
    

    def get(self, id):
        session = self.redis.get(id)
        if not session:
            raise RequestException("No se encontró la sesión de trivia que solicitaste", status_code=404)
        return self._deserialize(session)


    def submit(self, id, answers: List[AnswerSchema]):
        session = self.redis.get(id)
        if not session:
            raise RequestException("No se encontró la sesión de trivia que solicitaste", status_code=404)
        return self._evaluate(self._deserialize(session), answers)


    def _shuffle_options(self, challenge: TriviaChallenge):
        """
        Mezcla las opciones en el objeto challenge recibido, retorna el índice de las opciones correctas
        luego de ser mezcladas
        """
        random.shuffle(challenge.options)
        corrects = [i+1 for i in range(len(challenge.options)) if challenge.options[i].is_correct]
        challenge.options = [{"text": option["text"], "index": i} for i, option in enumerate(challenge.options, start=1)]
        return corrects


    def _generate_redis_key(self) -> int:
        while True:
            random_id = random.randint(1000, 9999)
            if self.redis.exists(random_id):
                continue
            return random_id


    def _serialize(self, challenge, corrects):
        return json.dumps(dict(challenge=challenge.to_mongo(), corrects=corrects))


    def _deserialize(self, values: str):
        return json.loads(values)


    def _evaluate(self, session, answers: List[AnswerSchema]):
        return [dict(id=answer.id, score=self._calculate_score(session.get("corrects"), answer.selected)) for answer in answers]


    def _calculate_score(self, corrects, selected):
        return len(self._intersection(corrects, selected)) / len(corrects) * 100


    def _intersection(self, x: list, y: list):
        return list(set(x) & set(y))
