#!/usr/bin/env python

from fastapi.responses import JSONResponse
from .handlers.handlers import map_handler

def _obj_to_dict(obj):
    """ Convierte un objeto en un diccionario. """
    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, dict):
        return {k: _obj_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple, set)):
        return [_obj_to_dict(e) for e in obj]
    else:
        return {k: _obj_to_dict(v) for k, v in vars(obj).items()}


async def _handle_exception(request, e):
    return map_handler(e)(request, e)


async def _handle_json_response(response):
    try:
        return JSONResponse(
            content=_obj_to_dict(response), 
            status_code=response.status_code if hasattr(response, "status_code") else 200)
    except:
        return response


async def _handle_plain_response(request, response):
    if isinstance(response, JSONResponse):
        return response

    if response.status_code == 404:
        if request.app.debug:
            return JSONResponse({"message": "resource not found", "available_endpoints": [route.path for route in request.app.routes]})
        else:
            return response
    
    if response.status_code == 500:
        if request.app.debug:
            return JSONResponse(
                content=_obj_to_dict(response),
                status_code=response.status_code if hasattr(response, "status_code") else 500)
        else:
            return JSONResponse(
                {"message": "An internal server error has occurred"},
                status_code=500)  

    return response


async def response_handler(request, call_next):
    try:
        response = await call_next(request)
    except Exception as e:
        return await _handle_exception(request, e)

    content_type = response.headers.get("content-type")
    if content_type and "application/json" in content_type:
        return await _handle_json_response(response)
    else:
        return await _handle_plain_response(request, response)
