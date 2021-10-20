import random


def generate_verification_code_v1():
    '''随机生成6位的验证码'''
    code_list = []
    for i in range(2):
        random_num = str(random.randint(0, 9))
        random_uppercase_letter = chr(random.randint(65, 90))
        random_lowercase_letter = chr(random.randint(97, 122))
        code_list.append(random_num)
        code_list.append(random_uppercase_letter)
        code_list.append(random_lowercase_letter)
    verification_code = ''.join(code_list)
    return verification_code


def generate_verification_code(len=6):
    '''
    随机生成6位的验证码
    '''
    code_list = []
    # 0-9
    for i in range(10):
        code_list.append(str(i))
    # A-Z
    for i in range(65, 91):
        code_list.append(chr(i))
    # a-z
    for i in range(97, 123):
        code_list.append(chr(i))
    return ''.join(random.sample(code_list, len))


if __name__ == '__main__':
    for i in range(1, 10):
        print(generate_verification_code())
