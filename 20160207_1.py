#_*_ coding: utf-8 _*_

print "g"

f = lambda x: x+1
print f(1)

g = lambda x,y: x+y
print g(1,2)


incr = lambda x,inc=1: x+inc
print incr(10)
print incr(10, 5)

vargs = lambda x, *args: args
print vargs(1,2,3,4,5)

def f1(x):
	return x*x + 3*x - 10

def f2(x):
	return x*x*x

def g(func):
	return [func(x) for x in range(-10,10)]

print g(f1)
print g(f2)

print [x+x for x in range(0,10)]

print g(lambda x: x*x + 3*x - 10)
print g(lambda x: x*x*x)

