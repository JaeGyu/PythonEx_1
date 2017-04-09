class MyClass:
    name = "alice"
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def say_hello(self):
        self.greet = "Hello"
    
    def say_hi(self):
        print("HI~~~~~")
        


p1 = MyClass()
p2 = MyClass()

print(p1.name)
p1.set_name("bob")
print(p1.name)

print(p2.name)

# 인스턴스 멤버를 적용한후에 그 인스턴스 멤버에 접근 할 수 있다
p1.say_hello()
print(p1.greet)

#클래스 메서드를 클래스. 으로 호출 했기 떄문에 self 파라미터를 하나 넘겨 줘야 한다 
MyClass.say_hi("gg")

