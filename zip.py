indexes = [0, 1, 2, 3]
alphabet = ['a', 'b', 'c']


def main():
    zip_result = zip(indexes, alphabet)
    for a, b in zip_result:
        print(a, b)
    print(list(zip_result))

    print(list(zip(alphabet, indexes)))


if __name__ == '__main__':
    main()
