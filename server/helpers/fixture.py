#!/usr/bin/env python

from ..api.challenge.model import Challenge, File
from ..api.user.model import User

### example mongo challenge ###

challenge = Challenge(
    _id=1,
    name='Mi primer Challenge',
    solution=[
        File(
            filename='archivo1.py',
            type='file',
            content='def es_par(n):\n    return n % 2 == 0',
        )
    ],
    tests=[
        File(
            filename='test1.py',
            type='file',
            content='from .archivo1.py import es_par\nfrom testing.assertions import *\ndef test_es_par():\n    assert_true(es_par(2), "El numero deberia ser par", json_metadata)\n    assert_false(es_par(3), "El numero deberia ser impar", json_metadata)'
        )
    ],
    clean_db=True,
    encapsulate_in_fn=False,
    avoid_main=False
)

try:
    challenge.save()
    print("Saved challenge:", challenge.to_mongo())
except:
    print("Fixture challenge already exists")

### example mongo user ###

user = User(
    username='tester',
    solutions=[]
)

try:
    user.save()
    print("Saved user:", user.to_mongo())
except:
    print("Fixture user already exists")