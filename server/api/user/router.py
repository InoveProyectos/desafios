#!/usr/bin/env python

from fastapi import APIRouter

from .controller import get, create

router = APIRouter()

router.get("/{user_id}", status_code = 200)(get)

router.post("/", status_code = 201)(create)
