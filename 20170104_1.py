
outter = 77

def func():
    global outter
    outter += 23
    print(outter)

func()

outData = [77]

def func2(param):
    param[0] += 23
    print(param)

func2(outData)

class A(object):
    def whoami(self):
        return self.__class__.__name__
    
a = A()
print(a.whoami())

class Abcdefg(A):
    pass

abc = Abcdefg()
print(abc.whoami())

def func3(x):
    return x**2

print(func3(3))
print((lambda x : x**2)(3))

lambda_v = lambda x,y : x+y

print(lambda_v(3,4))
