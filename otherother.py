def func(x):
    def func2(y):
        print(x + y)
    return func2

x = func(5)
x(3)

func(1)(9)