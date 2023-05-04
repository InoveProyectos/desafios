#!/usr/bin/env python

from fastapi import APIRouter

from .controller import *

router = APIRouter()

controller = UserController()

router.get("/", status_code = 200)(controller.get_all)

router.get("/{id}", status_code = 200)(controller.get)

router.post("/", status_code = 201)(controller.create)

router.patch("/{id}", status_code = 200)(controller.update)

router.delete("/{id}", status_code = 200)(controller.delete)

router.get("/{id}/score", status_code =200)(controller.get_score)