alphabet = ['a', 'b', 'c', 'c']

duplicates = set([x for x in alphabet if alphabet.count(x) > 1])


colors = set(['red', 'green', 'blue'])
colours = set(['red', 'yellow', 'cyan'])

if __name__ == '__main__':
    print(duplicates, set(alphabet))

    print('intersection', colors.intersection(colours))
    print('difference', colors.difference(colours))
