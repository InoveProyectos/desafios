#!/usr/bin/env python

from mongoengine import Document, StringField, IntField, SequenceField

class User(Document):
    _id = SequenceField(required = True, primary_key = True, sequence_name="user_sequence")
    username = StringField(required = True, unique = True)
    score = IntField(required = True)
