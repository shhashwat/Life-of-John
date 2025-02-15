x = 'tim'

def getName(name):
    global x
    x = name

print(x)
getName('bob')
print(x)