#!/usr/bin/env python

from .user.router import router as users
from .challenge.router import router as challenges
from fastapi import APIRouter

router = APIRouter()

router.include_router(users, prefix="/users", tags=["users"])
router.include_router(challenges, prefix="/challenges", tags=["challenges"])
