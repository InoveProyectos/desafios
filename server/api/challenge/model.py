#!/usr/bin/env python

from mongoengine import (
  Document,
  StringField,
  SequenceField,
  EmbeddedDocument,
  EmbeddedDocumentListField,
  BooleanField,
)


class File(EmbeddedDocument):
    filename = StringField(required=True)
    type = StringField(required=True)
    content = StringField(required=True)


class SolutionFile(EmbeddedDocument):
    filename = StringField(required=True)
    type = StringField(required=True)
    content = StringField(required=True)
    clean_db = BooleanField(required=True, default=False)
    avoid_main = BooleanField(required=True, default=False)
    encapsulate_in_fn = BooleanField(required=True, default=False)


class Challenge(Document):
    _id = SequenceField(required = True, primary_key = True, sequence_name="challenge_sequence")
    name = StringField(required=True)
    solution = EmbeddedDocumentListField(SolutionFile, required=True)
    tests = EmbeddedDocumentListField(File, required=True)
    meta = {'collection': 'challenges'}
