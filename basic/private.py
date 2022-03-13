class Foo:
    def __private(self):
        print('private')


if __name__ == '__main__':
    foo = Foo()
    foo.__private()
    foo._Foo__private()
