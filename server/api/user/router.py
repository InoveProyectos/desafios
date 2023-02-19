#!/usr/bin/env python

from fastapi import APIRouter

from .controller import *

router = APIRouter()

controller = UserController()

router.get("/", status_code = 200)(controller.get_all)

router.get("/{user_id}", status_code = 200)(controller.get)

router.post("/", status_code = 201)(controller.create)

router.patch("/{user_id}", status_code = 200)(controller.update)

router.delete("/{user_id}", status_code = 200)(controller.delete)
