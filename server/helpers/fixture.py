#!/usr/bin/env python

from ..api.challenge.model import Challenge, Solution, Test
from ..api.user.model import User

### example mongo challenge ###

challenge = Challenge(
    name='Mi primer Challenge',
    solution=[
        Solution(
            filename='archivo1.py',
            type='Python',
            content='print("Hola, Mundo!")',
            clean_db=True,
            encapsulate_in_fn=False,
            avoid_main=False
        )
    ],
    tests=[
        Test(
            filename='test1.py',
            content='assert True'
        )
    ]
)

challenge.save()

### example mongo user ###

user = User(
    username='tester',
    score=70
)

user.save()