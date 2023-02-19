#!/usr/bin/env python

from fastapi import APIRouter

from .controller import *

router = APIRouter()

controller = ChallengeController()

router.get("/", status_code = 200)(controller.get_all)

router.get("/{challenge_id}", status_code = 200)(controller.get)

router.post("/", status_code = 201)(controller.create)

router.patch("/{challenge_id}", status_code = 200)(controller.update)

router.delete("/{challenge_id}", status_code = 200)(controller.delete)

router.post("/{challenge_id}/submit/{user_id}", status_code = 200)(controller.submit)