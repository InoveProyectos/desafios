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
        user = User(username=data.username, score=0)
        return user.save().to_mongo()


    async def update(self, id, data: UserSchema):
        user = User.objects.get(_id=id)
        return user.update(**data.dict(exclude_unset=True)).to_mongo()


    async def delete(self, user_id):
        user = User.objects.get(_id=user_id)
        return user.delete().to_mongo()
