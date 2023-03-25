#!/usr/bin/env python

from fastapi.responses import JSONResponse

def handle_exception(request, exc):
    return JSONResponse({"message": str(exc) if str(exc) else "Internal server error"}, status_code = 500)

def handle_value_error(request, exc):
    return JSONResponse({"message": "ValueError", "errors": str(exc)}, status_code = 500)
