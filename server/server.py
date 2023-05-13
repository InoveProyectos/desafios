#!/usr/bin/env python

from .api import router as api_router
from .config import *
from .middleware import response_handler

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect, errors

connect(host = connections['mongo']['uri'])

app = FastAPI(debug=debug, docs_url="/index.html")

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

# redirect / and /docs to /index.html
app.add_api_route("/", endpoint=lambda: RedirectResponse(url="/index.html"), include_in_schema=False)
app.add_api_route("/docs", endpoint=lambda: RedirectResponse(url="/index.html"), include_in_schema=False)

# /api routes
app.include_router(api_router, prefix = "/api")

if mode == "development":
    try:
        from .helpers import fixture
    except errors.NotUniqueError:
        print("fixtures already loaded")