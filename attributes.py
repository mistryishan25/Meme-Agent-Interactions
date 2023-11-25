from enum import Enum


class Anonymity(Enum):
    NOT = 0.0
    MOSTLY_NOT = 0.25
    SOMEWHAT = 0.5
    VERY = 0.75
    FULLY = 1.0


class Ideology(Enum):
    ALT_RIGHT = 0.0
    CONSERVATIVE = 0.25
    MODERATE = 0.5
    LIBERAL = 0.75
    LEFTIST = 1.0


class Susceptability(Enum):
    NEVER = 0.0
    INFREQUENTLY = 0.25
    SOMETIMES = 0.5
    FREQUENTLY = 0.75
    ALWAYS = 1.0


class Racism(Enum):
    ANTI = 0.0
    AGAINST = 0.25
    NEUTRAL = 0.5
    SOFT = 0.75
    HARD = 1.0


class States(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2
