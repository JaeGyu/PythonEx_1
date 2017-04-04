def func():
    print("Hello")


def func2():
    print("world")
l = [1,2,3,func, lambda x: x+1]

print(l)
print(l[3]())
print(l[4](2))

l2 = [func, func2]

for i in l2:
    i()