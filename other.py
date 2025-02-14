x = [[x + 5 for x in range(3)] for y in range(3)]

y = [y for y in range(100) if y%5 == 0]
t = {i:i for i in range(100) if i%5 == 0}
s = {i for i in range(100) if i%5 == 0}
a = tuple(i for i in range(100) if i%10 == 0)

print(a)