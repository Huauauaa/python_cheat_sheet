from enum import Enum, auto, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


@unique
class Type(Enum):
    A = 1
    B = 2


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


if __name__ == '__main__':
    pass
