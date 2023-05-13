#!/usr/bin/env python

from .api import router as api_router
from .config import *
from .middleware import response_handler

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect, errors

connect(host = connections['mongo']['uri'])

app = FastAPI(debug=True, docs_url="/index.html")

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

app.middleware("http")(response_handler)
app.include_router(api_router, prefix = "/api")

if mode == "development":
    try:
        from .helpers import fixture
    except errors.NotUniqueError:
        print("fixtures already loaded")