#!/usr/bin/env python


from fastapi import APIRouter

from .controller import TriviaChallengeController
from .session import router as session_router

router = APIRouter()

controller = TriviaChallengeController()

router.get("/", status_code = 200)(controller.get_all)

router.get("/{id}", status_code = 200)(controller.get)

router.post("/", status_code = 201)(controller.create)

router.patch("/{id}", status_code = 200)(controller.update)

router.delete("/{id}", status_code = 200)(controller.delete)

# Session's endpoints
router.include_router(session_router, prefix="/session")