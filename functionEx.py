#_*_ coding: utf-8 _*_

a = 1
b = 1

def vartest():
	global a
	a= a+1

vartest()

def vartest2(a):
	return a+1;

print vartest2(b)
print a