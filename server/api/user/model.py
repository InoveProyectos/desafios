#!/usr/bin/env python

from mongoengine import Document, StringField, IntField

class User(Document):
    username = StringField(required = True, unique = True)
    score = IntField(required = True)
