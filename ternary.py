# Blueprint

# value_if_true if condition else value_if_false

is_active = True

empty_dict = {}


if __name__ == '__main__':
    print('active' if is_active else 'inactive')
    print(('inactive', 'active')[is_active])
    print(empty_dict.get('id') or 'empty')
