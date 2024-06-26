#!/usr/bin/env python

from .model import User
from functools import reduce
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str

class UserController:

    async def get_all(self):
        users = User.objects.all()
        return [user.to_mongo() for user in users]


    async def get(self, user_id):
        user = User.objects.get(_id=user_id)
        return user.to_mongo()


    async def create(self, data: UserSchema):
        user = User(username=data.username, solutions=[])
        return user.save().to_mongo()


    async def update(self, id, data: UserSchema):
        user = User.objects.get(_id=id)
        return user.update(**data.dict(exclude_unset=True)).to_mongo()


    async def delete(self, user_id):
        user = User.objects.get(_id=user_id)
        return user.delete().to_mongo()
    

    async def get_score(self, user_id):
        user = User.objects.get(_id=user_id)
        return self._calculate_total_score(user)


    def _add_or_replace_solution(self, user_id, solution):
        """
        Agregar una solución al usuario, en caso de que ya existía una solución para ese
        challenge_id, reemplazarla con los nuevos valores
        """
        user = User.objects.get(_id=user_id)
        user.solutions.filter(challenge_id=solution.challenge_id).delete()
        user.solutions.append(solution)
        user.save()
        return user.to_mongo()


    def _calculate_total_score(self, user):
        """
        Calcular el puntaje total del usuario
        """
        return reduce(lambda acc, solution: acc + solution.score, user.solutions, 0)