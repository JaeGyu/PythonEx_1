class MyClass:
    name = "alice"
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name


p1 = MyClass()
p2 = MyClass()

print(p1.name)
p1.set_name("bob")
print(p1.name)

print(p2.name)



