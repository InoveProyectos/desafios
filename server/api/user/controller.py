#!/usr/bin/env python

from .model import User
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    score: int = 0


class UserController:

    async def get_all(self):
        users = User.objects.all()
        return [user.to_mongo() for user in users]


    async def get(self, user_id):
        user = User.objects.get(_id=user_id)
        return user.to_mongo()


    async def create(self, data: UserSchema):
        user = User(username=data.username, score=0, solutions=[])
        return user.save().to_mongo()


    async def update(self, id, data: UserSchema):
        user = User.objects.get(_id=id)
        return user.update(**data.dict(exclude_unset=True)).to_mongo()


    async def delete(self, user_id):
        user = User.objects.get(_id=user_id)
        return user.delete().to_mongo()


    def _add_or_replace_solution(self, user_id, solution):
        """
        Agregar una solución al usuario, en caso de que ya existía una solución para ese
        challenge_id, reemplazarla con los nuevos valores
        """
        user = User.objects.get(_id=user_id)
        user.solutions = [s for s in user.solutions if s.challenge_id != solution.challenge_id]
        user.solutions.append(solution)
        user.save()
        return user.to_mongo()
