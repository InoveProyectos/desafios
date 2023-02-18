#!/usr/bin/env python

from .model import User
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str


async def get(user_id):
    user = User.objects.get(_id=user_id)
    return user.to_mongo()


async def create(data: UserSchema):
    user = User(username=data.username, score=0)
    return user.save().to_mongo()
