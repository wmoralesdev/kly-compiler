from enum import Enum


class Object(Enum):
    CONST = 0
    VARIABLE = 1
    FUNCTION = 2
    PARAMETER = 3
    RETURN = 4
