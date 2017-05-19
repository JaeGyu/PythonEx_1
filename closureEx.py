def outter():
    message = "Hi"
    def inner():
        print(message) #inner함수 안에서 정의 되진 않았지만 inner에서 사용되었기 때문에 프리변수라 한다. 
    return inner()

outter()

def outter2():
    message = "Hi2"
    def inner2():
        print(message)
    return inner2

my_func = outter2() #아무것도 출력 안된다. 단지 inner2라는 객체를 리턴했기 때문

my_func()

print(my_func)
print(dir(my_func))
print(type(my_func.__closure__))
print(my_func.__closure__)
print(my_func.__closure__[0])
print(dir(my_func.__closure__[0]))
print(my_func.__closure__[0].cell_contents)


def outter3(tag):
    message = "Some txt"
    tag = tag

    def inner3():
        print("<{0}>{1}<{0}>".format(tag,message))
    
    return inner3

outter3("h1")()
outter3("p")()


def outter4(tag):
    #tag = tag
    def inner4(txt):    
        print("<{0}>{1}<{0}>".format(tag,txt))
    return inner4

outter4("h1")("Hello")
outter4("p")("world")
