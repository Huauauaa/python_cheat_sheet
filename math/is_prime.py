def is_prime(num):
    '''素数'''
    for item in range(2, int(num ** 0.5) + 1):
        if num % item == 0:
            return False

    return True if num != 1 else False


if __name__ == '__main__':
    print(is_prime(6))
    print(is_prime(37))
