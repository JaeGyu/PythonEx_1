#_*_ coding: utf-8 _*_

def add(a,b):
	return a+b

print add(1,2)
print add

f = add

print add is add
print add is f

def f(a,b):
	return a + b(a)

def add2(a):
	return 10+a

print f(1,add2)
print type(add)

def simple():
	pass

print simple()

def minus(a,b):
	return a-b

print minus(a=12,b=20)
print minus(b=20,a=12)

def incr(x, y=1):
	return x + y

print incr(5)
print incr(5,10)

def calc(x,y):
	return x+y,x-y,x*y,x/y

print calc(10,2)

def sum(N):
	if N == 1:
		return 1
	return N + sum(N-1)

print sum(10)


for i in range(2,20):
	for j in range(1,10):
		print i,'*',j,'=',i*j

for x in range(100):
	if x>10:
		break
	print x,

print 32500 /24
