from pipe import chain, dedup, groupby, select, uniq, where

numbers = list(range(4))


print('origin', numbers)

print('filter', list(numbers | where(lambda x: x % 2 == 0)))
print('map', list(numbers | select(lambda x: x * 2)))
print('filter&map', list(numbers | where(
    lambda x: x % 2 == 1) | select(lambda x: x * 2)))


print('chain', list([[1, 2], [2, 3]] | chain))

print('group', dict(numbers | groupby(lambda x: 'Even' if x %
      2 == 0 else 'odd') | select(lambda x: (x[0], list(x[1])))))


print('dedup', list([1, 2, 3, 3, 2] | dedup))
print('uniq ', list([1, 2, 3, 3, 2] | uniq))
