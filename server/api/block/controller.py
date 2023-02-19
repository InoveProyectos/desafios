#!/usr/env/bin python

from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from .model import ChallengeBlock
from ..challenge.model import Challenge
from ..challenge.controller import ChallengeSchema
from pydantic import BaseModel


class ChallengeBlockSchema(BaseModel):
    name: str
    challenges: List[ChallengeSchema]

class ChallengeBlockController:

    async def get_all(self):
        blocks = ChallengeBlock.objects.all()
        return [block.to_mongo() for block in blocks]


    async def get(self, block_id: str):
        block = ChallengeBlock.objects.get(_id=block_id)
        return block.to_mongo()


    async def create(self, block: ChallengeBlockSchema):
        new_block = ChallengeBlock(name=block.name, challenges=block.challenges)
        new_block.save()
        return new_block.to_mongo()


    async def update(self, block_id: str, block: ChallengeBlockSchema):
        block = ChallengeBlock.objects.get(_id=block_id)
        block.update(**block.dict(exclude_unset=True))
        return block.to_mongo()


    async def delete(self, block_id: str):
        block = ChallengeBlock.objects.get(_id=block_id)
        block.delete()
        return block.to_mongo()


    async def add_challenge_id(self, block_id: str, challenge_id: str):
        block = ChallengeBlock.objects.get(_id=block_id)
        challenge = Challenge.objects.get(id=ObjectId(challenge_id))
        block.challenges.append(challenge)


    async def add_challenge(self, block_id, challenge: ChallengeSchema):
        block = ChallengeBlock.objects.get(_id=block_id)
        challenge = Challenge(**challenge.dict())
        challenge.save()
        block.challenges.append(challenge)
        return block.to_mongo()
