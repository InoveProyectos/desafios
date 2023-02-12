#!/usr/bin/env python

from fastapi.responses import JSONResponse

async def handle_validation_error(request, exc):
    return JSONResponse({"message": "Error de validación", "errors": str(exc)})

async def handle_unique_error(request, exc):
    return JSONResponse({"message": "Estás intentando guardar un valor duplicado", "field_name": str(exc)})