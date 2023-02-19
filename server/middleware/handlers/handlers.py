#!/usr/bin/env python

from .errors import mongo, generic
from mongoengine.errors import ValidationError, NotUniqueError

def map_handler(error):
    if isinstance(error, ValidationError):
        return mongo.handle_validation_error
    if isinstance(error, NotUniqueError):
        return mongo.handle_unique_error
    if isinstance(error, ValueError):
        return generic.handle_value_error
    return generic.handle_exception