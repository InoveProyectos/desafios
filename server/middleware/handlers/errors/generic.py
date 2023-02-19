#!/usr/bin/env python

from fastapi.responses import JSONResponse

def handle_exception(request, exc):
    return JSONResponse({"message": "An internal server error has occurred"}, status_code = 500)

def handle_value_error(request, exc):
    return JSONResponse({"message": "ValueError", "errors": str(exc)}, status_code = 500)
