#!/usr/bin/env python

from fastapi import APIRouter

from .controller import get, create

router = APIRouter()

router.get("/{user_id}")(get)

router.post("/")(create)
