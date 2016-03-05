#_*_ coding: utf-8 _*_

class S1:
	a=1

print S1.a
print


S1.b=2
print S1.b
print 

print dir(S1)
del S1.b
print dir(S1)
