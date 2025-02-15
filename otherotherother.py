x = [x for x in range(10)]
print(x)
mp = filter(lambda i: i%2 == 0, x)
print(list(mp))