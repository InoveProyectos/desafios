#!/usr/bin/env python

from fastapi.responses import JSONResponse
from .handlers.handlers import map_handler

def __obj_to_dict__(obj):
    """ Convierte un objeto en un diccionario. """
    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, dict):
        return {k: __obj_to_dict__(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple, set)):
        return [__obj_to_dict__(e) for e in obj]
    else:
        return {k: __obj_to_dict__(v) for k, v in vars(obj).items()}


async def response_handler(request, call_next):
    try:
        response = await call_next(request)
    except Exception as e:
        return map_handler(e)(request, e)

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
                content = __obj_to_dict__(response),
                status_code = response.status_code if hasattr(response, "status_code") else 500)
        else:
            return JSONResponse(
                {"message": "An internal server error has occurred"},
                status_code=500)  

    content_type = response.headers.get("content-type")
    if content_type and "application/json" in content_type:
        try:
            return JSONResponse(
                content=__obj_to_dict__(response), 
                status_code=response.status_code if hasattr(response, "status_code") else 200)
        except:
            return response

    return response