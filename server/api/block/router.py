#!/usr/bin/env python

from fastapi import APIRouter

from .controller import *

router = APIRouter()

controller = ChallengeBlockController()

router.get("/", status_code = 200)(controller.get_all)

router.get("/{block_id}", status_code = 200)(controller.get)

router.post("/", status_code = 201)(controller.create)

router.patch("/{block_id}", status_code = 200)(controller.update)

router.delete("/{block_id}", status_code = 200)(controller.delete)

router.post("/{block_id}/challenges", status_code = 200)(controller.add_challenge)

router.post("/{block_id}/challenges/{challenge_id}", status_code = 200)(controller.add_challenge_id)
