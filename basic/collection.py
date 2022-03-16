def test():
    nums = [1, 3, 5, 7, 9]
    gen = (n for n in nums if n in nums)
    result = list(gen)
    print(f'restult: {result}')


def test1():
    nums = [1, 3, 5, 7, 9]
    gen = (n for n in nums if n in nums)
    nums = [1, 2, 3, 4]
    result = list(gen)
    print(f'restult1: {result}')


def test2():
    nums = [1, 3, 5, 7, 9]
    result = list(n for n in nums if n in nums)
    nums = [1, 2, 3, 4]
    print(f'restult2: {result}')


if __name__ == '__main__':
    test()
    test1()
    test2()
