from pprint import pp, pprint


def show(x):
    print(f'normal: {x}')


def show_repr(x):
    print(f'repr: {x!r}')


def test_print():
    d = {'x': 1, 'z': 3, 'y': 1}
    print(d)
    # sort key
    pprint(d)
    pp(d)


if __name__ == '__main__':
    show(1)
    show('1')
    show('')
    show('\xa0  ')

    show_repr(1)
    show_repr('1')
    show_repr('')
    show_repr('\xa0  ')

    test_print()
