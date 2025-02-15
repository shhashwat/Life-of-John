def func(a, b, c=None):
    print("Running",a, b, c)
    def func1():
        print("Running func1")
    func1()
    return a*b, a+b

r1, r2 = func(2, 3)
print(r1, r2)