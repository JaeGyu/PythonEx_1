def outter():
    a = 0
    
    for i in range(10):
        a+=1

    def inner():
        nonlocal a
        print(a)

    return inner


z1 = outter()
z1()
