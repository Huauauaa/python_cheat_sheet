def is_palindrome(num):
    '''判断一个数是不是回文数'''
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10

    return total == num


if __name__ == '__main__':
    print(is_palindrome(12121))
