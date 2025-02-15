def func(x,y):
    print(x,y)

x = [(1,2),(3,4),(5,6)]

for x in x:
    func(*x)

print()

func(**{'x':1,'y':2})