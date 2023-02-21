# 03_namedtuple_typing.py

# How do you type hint a named tuple?

"""
A)

from collections import namedtuple

point = namedtuple("Point", ("x:int", "y:int"))

B)

from collections import namedtuple

point: namedtuple[int, int] = namedtuple("Point", ("x", "y"))

C)

from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int
"""


