#!/usr/bin/env python

from .errors import routing, mongo, generic
from fastapi import FastAPI
from mongoengine.errors import ValidationError, NotUniqueError

def register_handlers(app: FastAPI):
    app.add_exception_handler(404, routing.not_found)
    app.add_exception_handler(ValidationError, mongo.handle_validation_error)
    app.add_exception_handler(NotUniqueError, mongo.handle_unique_error)
    app.add_exception_handler(ValueError, generic.handle_value_error)
    app.add_exception_handler(Exception, generic.handle_exception)