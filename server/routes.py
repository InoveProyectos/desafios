#!/usr/bin/env python

from .api.user.router import router as users
from fastapi import APIRouter

router = APIRouter()

router.include_router(users, prefix="/users", tags=["users"])
