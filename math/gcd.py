def gcd(x, y):
    '''求最大公约数'''
    (x, y) = (x, y) if x < y else (y, x)
    for item in range(x, 0, -1):
        if x % item == 0 and y % item == 0:
            return item


if __name__ == '__main__':
    print(gcd(25, 35))
    print(gcd(35, 25))
    print(gcd(-35, 25))
