from enum import Enum


class Anonymity(Enum):
    """Anonymity characteristics for Agents"""
    NOT = 0.0
    MOSTLY_NOT = 0.25
    SOMEWHAT = 0.5
    VERY = 0.75
    FULLY = 1.0


class Ideology(Enum):
    """Ideology characteristics for Agents and Memes"""
    ALT_RIGHT = 0.0
    CONSERVATIVE = 0.25
    MODERATE = 0.5
    LIBERAL = 0.75
    LEFTIST = 1.0


class Susceptability(Enum):
    """Susceptability characteristics for Agents"""
    NEVER = 0.0
    INFREQUENTLY = 0.25
    SOMETIMES = 0.5
    FREQUENTLY = 0.75
    ALWAYS = 1.0


class Racism(Enum):
    """Racial bias characteristics for Agents and Memes"""
    ANTI = 0.0
    AGAINST = 0.25
    NEUTRAL = 0.5
    SOFT = 0.75
    HARD = 1.0


class States(Enum):
    """Valid Agent states"""
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2
