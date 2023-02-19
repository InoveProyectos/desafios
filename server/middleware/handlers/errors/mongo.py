#!/usr/bin/env python

from fastapi.responses import JSONResponse

def handle_validation_error(request, exc):
    return JSONResponse({"message": "Error de validación", "error": str(exc)}, status_code = 422)

def handle_unique_error(request, exc):
    return JSONResponse({"message": "Estás intentando guardar un valor duplicado", "error": str(exc)}, status_code = 422)

def handle_not_found_error(request, exc):
    return JSONResponse({"message": "No se encontró el recurso", "error": str(exc)}, status_code = 404)