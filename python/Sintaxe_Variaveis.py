
class MyClass():
    a = 10
    b = 3
    print(a+b)

    if 1 == 1:
        a = a - 1
        b = a + 10

        try:
            pass
        except Exception as e:
            raise e

        print(a)
        print(b)

a = 15
print(type(a))

a = '15'
print(type(a))

a = 1.5
print(type(a))

a = ['Item 1', 'Item 2', 'Item 3']
print(type(a))

a = ('Item 1', 'Item 2', 'Item 3')
print(type(a))

a = {1: 'Fulano', 2: 'Beltrano'}
print(type(a))

