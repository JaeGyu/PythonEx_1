param = 10
str_data = '전역변수'

def func1():
    str_data = "지역변수"
    print(str_data)

def func2(param):
    param = 1
    
    
def func3():
    global param
    param = 50

def func4():
    global temp
    temp = 150

def func5():
    param = 1000

def func6():
    print(str_data)


def func7():
    name = "alice"
    def func8():
        global name
        name = "bob"
    
    func8()
    print(name)
    

func1()
print(str_data)
print(param)
func2(param)
print(param)
func3()
print(param)
func4()
print(temp)
func5()
print(param)
func6()
func7()
print(name)

a,b,c = (3,2,1)

print(a,b,c)