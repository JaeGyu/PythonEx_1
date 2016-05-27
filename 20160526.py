#_*_ coding: utf-8 _*_

def f(**args):
	print(args)

f(a=1,b=2)

def my_func(param):
	param = "ff"
	print(param)
	print(id(param))
	print("-"*10)

param = '11'
print(id(param))
my_func(param)
print(id(param))