from functools import reduce


flowers = ['rose', 'tulip', 'Narcissus']
numbers = [1, 2, 3, 4]
me = {'name': 'Harvey', 'age': 30}
animals = ('dog', 'cat', 'cock', 'ox')

persons = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Doe'},
    {'id': 3, 'name': 'Dummy'},
]

upper_flowers = list(map(lambda item: item.upper(), flowers))
even_numbers = list(filter(lambda item: item % 2 == 0, numbers))
odd_numbers = [item for item in numbers if item % 2 == 1]
short_animals = list(filter(lambda item: len(item) <= 3, animals))

sum = reduce(lambda x, y: x + y, numbers)

me_keys = list(map(lambda key: key, me))

if __name__ == '__main__':

    print(flowers, upper_flowers, [x.upper() for x in flowers])
    print(numbers, even_numbers, sum, odd_numbers)
    print(me, me_keys, me.keys())
    print(animals, short_animals)

    print([person.get('name') for person in persons if person['id'] % 2 == 1])
