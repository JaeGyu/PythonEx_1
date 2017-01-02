var = 77

def func():
    global var
    var = 100
    print(locals())

func()

print(var)
