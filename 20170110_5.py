
def co_routine():
    total = 0
    while True:
        n = (yield)
        total += n
        print("total = " , total)

a = co_routine()

a.__next__()
a.send(1)
a.send(1)
a.send(3)

print(type(a))