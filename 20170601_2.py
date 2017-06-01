
a=1

def func(a):
    a+=1
    return a

def gFunc():
    global a
    a+=1
    return a


def gFunc2():
    global b
    b+=1

print(gFunc2())

print(func(a))
print(gFunc())
print(a)

