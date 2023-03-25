#!/usr/bin/env python

from mongoengine import (
  Document,
  StringField,
  SequenceField,
  EmbeddedDocument,
  EmbeddedDocumentListField,
  BooleanField,
  IntField
)

class Option(EmbeddedDocument):
    text = StringField(required=True)
    is_correct = BooleanField(required=True)


class TriviaChallenge(Document):
    _id = SequenceField(required = True, primary_key = True, sequence_name="trivia_challenge_sequence")
    name = StringField(required=True)
    statement = StringField(required=True)
    options = EmbeddedDocumentListField(Option, required=True)

    meta = {'collection': 'trivia_challenges'}
