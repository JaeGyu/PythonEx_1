#-*- codingLutf-8 -*-

h=5

def f(a):
	global h
	h=a+10
	return h

print f(10)
print h
