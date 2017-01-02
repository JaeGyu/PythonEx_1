
gb = 1

def func():
    a = 1
    print("dir() : ", dir())
    print("locals() : ",locals())
    print("globlas() : ", globals())

func()

g = globals()

print(g["__builtins__"])

print(dir(__builtins__))
print(__builtins__)

for i in dir(__builtins__):
    print(i)

