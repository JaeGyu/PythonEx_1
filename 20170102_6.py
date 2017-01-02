a = 1

print(dir(locals))

for i in dir(locals):
    print(i)

def func():
    b = 1
    print("dir :: ", dir(locals))

func()