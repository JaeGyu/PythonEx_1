dict1 = {'a':1}

print(len(dict1))

def func():
    print("hello")
    
dict1[func] = "world"

print(dict1)

def func2():
    print("world")

