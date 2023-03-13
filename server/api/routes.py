#!/usr/bin/env python

from .user import router as users
from .challenge import router as challenges
from .trivia import router as trivia
from fastapi import APIRouter

router = APIRouter()

router.include_router(users, prefix="/users", tags=["users"])
router.include_router(challenges, prefix="/challenges", tags=["challenges"])
router.include_router(trivia, prefix="/trivia", tags=["trivia"])