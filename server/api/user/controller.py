#!/usr/bin/env python

from .model import User
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class UserSchema(BaseModel):
    username: str


async def get(user_id):
    try:
        user = User.objects.get(_id=user_id)
        return user.to_mongo().to_dict()
    except User.DoesNotExist:
        return JSONResponse({"message": "User not found"}, status_code=404)


async def create(data: UserSchema):
    user = User(username=data.username, score=0)
    user.save()
    return user.to_mongo().to_dict()
