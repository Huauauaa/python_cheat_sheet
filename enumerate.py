fruits = ['apple', 'pear', 'banana']


def main():
    for index, value in enumerate(fruits):
        print(index, value)

    for index, value in enumerate(fruits, 10):
        print(index, value)


if __name__ == '__main__':
    main()
