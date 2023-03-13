#!/usr/bin/env python


from fastapi import APIRouter

from .controller import TriviaChallengeController

router = APIRouter()

controller = TriviaChallengeController()

router.get("/", status_code = 200)(controller.get_all)

router.get("/{challenge_id}", status_code = 200)(controller.get)

router.post("/", status_code = 201)(controller.create)

router.patch("/{challenge_id}", status_code = 200)(controller.update)

router.delete("/{challenge_id}", status_code = 200)(controller.delete)

# TODO: get and create session

# TODO: submit answer