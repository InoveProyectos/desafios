#!/usr/bin/env python

from ..api.challenge.model import Challenge, File
from ..api.user.model import User

### example mongo challenge ###

challenge = Challenge(
    name='Mi primer Challenge',
    solution=[
        File(
            filename='archivo1.py',
            type='Python',
            content='print("Hola, Mundo!")',
        )
    ],
    tests=[
        File(
            filename='test1.py',
            content='assert True'
        )
    ],
    clean_db=True,
    encapsulate_in_fn=False,
    avoid_main=False
)

challenge.save()

### example mongo user ###

user = User(
    username='tester',
    score=70,
    solutions=[]
)

user.save()