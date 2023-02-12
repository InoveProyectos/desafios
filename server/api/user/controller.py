#!/usr/bin/env python

from mongoengine import ValidationError
from .model import User
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class UserSchema(BaseModel):
    username: str


async def get(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return JSONResponse({"message": "User not found"}, status_code=400)
    except ValueError:
        return JSONResponse({"message": "Invalid user ID provided, expected a hexadecimal UUID string"}, status_code=400)


async def create(data: UserSchema):
    user = User(username=data.username, score=0)
    try:
        user.save()
        return user.to_mongo().to_dict()
    except ValidationError as e:
        return e