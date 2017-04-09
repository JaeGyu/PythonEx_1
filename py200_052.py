class MyClass:
    def __init__(self):
        self.__name = "Alice"  #인스턴스 멤버의 접근제어자를 private로 한다 
    
    def get_name(self):
        return self.__name

p = MyClass()

print(p.get_name())
# print(p.__name)  #접근제어자 때문에 오류남

