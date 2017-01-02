

def func(a):
    return a()


def func2():
    print("test")

func(func2)

