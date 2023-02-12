#!/usr/bin/env python

from fastapi import FastAPI
from starlette.responses import JSONResponse

async def not_found(request, exc):
    app = request.app
    endpoints = [route.path for route in app.routes]
    return JSONResponse(content = {"message": "resource not found", "available_endpoints": endpoints}, status_code = 404)
