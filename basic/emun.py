

from enum import Enum, auto, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 专用于枚举的 class 装饰器。 它会搜索一个枚举的 __members__ 并收集所找到的任何别名；只要找到任何别名就会引发 ValueError 并附带相关细节信息:


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

    print(Color.RED, repr(Color.RED), type(Color.RED), isinstance(
        Color.GREEN, Color), Color.RED.name)

    for color in Color:
        print(color)

    for i in range(1, 3):
        print(Color(i))

    member = Color.RED
    print(member.name, member.value)

    car = {
        'color': Color.RED.value
    }
    print(car)
    print(Type.A)
    print(list(Ordinal))

    for name, member in Ordinal.__members__.items():
        print(name, member)

    # 比较
    print(Color.RED is Color.BLUE)
