#!/usr/bin/env python

from .handlers.register import register_handlers
from .routes import router
from .config.environment import *

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect, errors

connect(host = mongo['uri'])

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

register_handlers(app)
app.include_router(router, prefix = "/api")