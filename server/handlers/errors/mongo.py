#!/usr/bin/env python

from fastapi.responses import JSONResponse

async def handle_validation_error(request, exc):
    return JSONResponse({"message": "Error de validación", "error": str(exc)}, status_code = 422)

async def handle_unique_error(request, exc):
    return JSONResponse({"message": "Estás intentando guardar un valor duplicado", "error": str(exc)}, status_code = 422)