from __future__ import print_function

def print_name(_name):
    print("name은 %s 입니다 " % _name)
    
def print_age(_age):
    print("age는 %s 입니다 " % _age)

name = "alice"
age = 34

print_name(name)

name = input("name : ")
print_name(name)

old = input("age : ")
print_age(old)
