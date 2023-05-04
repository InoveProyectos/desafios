#!/usr/bin/env python

from mongoengine import (
    Document,
    StringField,
    IntField,
    SequenceField,
    EmbeddedDocumentListField,
    EmbeddedDocument)


class File(EmbeddedDocument):
    filename = StringField(required=True)
    type = StringField(required=True)
    content = StringField(required=True)


class Solution(EmbeddedDocument):
    challenge_id = IntField(required=True)
    files = EmbeddedDocumentListField(File, required=True)
    score_earned = IntField(required=True)


class User(Document):
    _id = SequenceField(required=True, primary_key=True, sequence_name="user_sequence")
    username = StringField(required=True, unique=True)
    solutions = EmbeddedDocumentListField(Solution, default=[])

    meta = {'collection': 'users'}
 