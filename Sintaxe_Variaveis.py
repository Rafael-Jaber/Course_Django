
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