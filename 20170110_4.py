def my_gen():
    n = 0
    while n<=2:
        yield n
        n+=1

a = my_gen()

print(type(a))

print(a.__next__())
print(a.__next__())
print(a.__next__())

def my():
    pass

print(type(my))

def my_gen2():
    n=0
    b=1
    yield n
    yield b

b = my_gen2()
print(type(b))
print(b.__next__())
print(b.__next__())

"""
무한대 제네레이터
"""
def my_gen3():
    n = 0
    while True:
        yield n
        n+=1

c = my_gen3()

for i in range(100):
    print(c.__next__())