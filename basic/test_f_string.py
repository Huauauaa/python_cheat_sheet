# %-formatting

name = 'Harvey'

print('Hello1, %s.' % name)

age = 20

print('Hello2, %s. You are %s.' % (name, age))


# str.format()

print('Hello3, {}. You are {}.'.format(name, age))
print('Hello4, {1}. You are {0}.'.format(age, name))

author = {'name': name, 'age': age}

print('Hello5, {name}. You are {age}.'.format(name=author['name'], age=author['age']))
# use ** to do this neat trick with dictionaries
print('Hello6, {name}. You are {age}.'.format(**author))

# f-Strings
print(f'Hello7, {name}. You are {age}.')
# It would also be valid to use a capital letter F
print(F'Hello8, {name}. You are {age}.')
print(f'{2*3}')


def to_uppercase(input):
    return input.upper()


print(f'{to_uppercase(name)} is a nice guy.')


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_comedian = Comedian("Harvey", "Hua", "20")
print(f'{new_comedian}')
print(f'{new_comedian!r}')

affiliation = 'Huauauaa'
message = f'''
Hi {name}.
You are {age}. 
You were in {affiliation}.
'''


print(message)


import timeit

time_number = 1_000_000
result = timeit.timeit(
    '''name = 'Harvey'
age = 30
'%s is %s.' % (name, age)
''',
    number=time_number,
)

print(result)

result = timeit.timeit(
    '''name = 'Harvey'
age = 30
'{} is {}.'.format(name, age)
''',
    number=time_number,
)

print(result)

result = timeit.timeit(
    '''name = 'Harvey'
age = 30
f'{name} is {age}.'
''',
    number=time_number,
)

print(result)
