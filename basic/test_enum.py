from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WENTER = 4


Animal = Enum('Animal', 'ANT BEE CAT DOG')


if __name__ == '__main__':
    result = []
    for k, v in Season.__members__.items():
        result.append((v.value, k))

    print(tuple(result))
    # print(Animal, Animal.ANT, Animal.ANT.value)
