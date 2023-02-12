#!/usr/bin/env python

from fastapi.responses import JSONResponse

async def handle_exception(request, exc):
    return JSONResponse({"message": "An internal server error has occurred"})