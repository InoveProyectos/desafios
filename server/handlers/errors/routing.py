#!/usr/bin/env python

from fastapi.responses import JSONResponse

async def not_found(request, exc):
    app = request.app
    endpoints = [route.path for route in app.routes]
    return JSONResponse({"message": "resource not found", "available_endpoints": endpoints})
