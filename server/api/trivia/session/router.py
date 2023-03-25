#!/usr/bin/env python

from fastapi import APIRouter

from .controller import SessionController

router = APIRouter()

controller = SessionController()

router.post("/", status_code = 200)(controller.create)

router.get("/{id}", status_code = 200)(controller.get)

router.post("/{id}", status_code = 201)(controller.submit)
