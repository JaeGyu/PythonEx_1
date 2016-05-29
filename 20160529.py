#_*_ coding: utf-8 _*_
print("hh")

def my_func():
	print(param)
	print(id(param))

param = "한재규"
my_func()

print("외부에서 찍힌 값 : ",id(param))


def my_fun2():
	print(param2)

param2 = "hh"
my_fun2()

print("-"*40)

def my_fun3():
	global param3
	print(param3)
	print(id(param3))

param3 = "qq"
my_fun3()
print(param3)
print(id(param3))
