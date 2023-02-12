#!/usr/bin/env python

from fastapi.responses import JSONResponse

async def handle_exception(request, exc):
    return JSONResponse({"message": "An internal server error has occurred"}, status_code = 500)

async def handle_value_error(request, exc):
    return JSONResponse({"message": "Error de valor", "errors": str(exc)}, status_code = 500)