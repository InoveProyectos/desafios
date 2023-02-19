#!/usr/bin/env python

from mongoengine import (
  Document,
  StringField,
  SequenceField,
  EmbeddedDocument,
  EmbeddedDocumentListField,
  BooleanField
)

class Test(EmbeddedDocument):
    filename = StringField(required=True)
    type = StringField(required=True)
    content = StringField(required=True)


class Solution(EmbeddedDocument):
    filename = StringField(required=True)
    type = StringField(required=True)
    content = StringField(required=True)
    clean_db = BooleanField(default=False)
    encapsulate_in_fn = BooleanField(default=False)
    avoid_main = BooleanField(default=False)


class Challenge(Document):
    _id = SequenceField(required = True, primary_key = True, sequence_name="challenge_sequence")
    name = StringField(required=True)
    solution = EmbeddedDocumentListField(Solution, required=True)
    tests = EmbeddedDocumentListField(Test, required=True)
