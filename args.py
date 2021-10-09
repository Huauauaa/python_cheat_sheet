def play_card(*args):
    for c in args:
        print(c)


def discard_card(**kwargs):
    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key])


if __name__ == '__main__':
    # play_card('Club A')
    # play_card(
    #     'Heart 2',
    #     'Heart 3',
    #     'Heart 4',
    # )

    cards = ['Spade J', 'Diamond J']
    card = {'suit': 'Diamond', 'number': 3}

    # print('card: %s', *card)

    # play_card(cards)
    # play_card(*cards)

    discard_card(**card)
