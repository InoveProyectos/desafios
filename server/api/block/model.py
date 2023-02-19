#!/usr/bin/env python

from mongoengine import Document, StringField, ListField, ReferenceField, SequenceField

class ChallengeBlock(Document):
    _id = SequenceField(required = True, primary_key = True, sequence_name="user_sequence")
    name = StringField(required=True)
    challenges = ListField(ReferenceField('ChallengeModel'))
