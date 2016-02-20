#_*_ coding: utf-8 _*_

def incr(a, step=1):
	return a+step

b = 1
b = incr(b)
print b

b = incr(b, 10)
print b

def incr(a,step=1,step2=10):
	return a+step+step2

print "result :: %d" % (incr(1,step2=10),)

print "%d %d" % (2,3)

print type((1,))


print incr(1,2)

def area(h,w):
	return h*w

a = area(h='fff',w=3)
print a

b = area(w=20,h=10)
print b

print area(50,w=5)
print area(h=2,w=3)


def incr(a,step=1,step2=10,step3=100):
	return a+step+step2+step3

print incr(10,2,step2=100)
print incr(10,step2=100,step3=200)

def varg(a, *arg):
	print a,arg

varg(1)
varg(2,3)
varg(1,2,3)
varg(1,2,3,4,5,6,7,8,9)

def varg(*arg):
	print arg

varg(1,2,3)

def printf(format,*args):
	print format % args

printf("I've sdf %d asdf %d",6,5)

def h(a,b,c):
	print a,b,c

args = (1,2,3)
h(*args)

dargs = {'a':1,'b':2,'c':3}
h(**dargs)




