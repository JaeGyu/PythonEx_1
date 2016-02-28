
#-*- coding:utf-8 -*-

class C:
	a=2
	pass

c = C()
print c.a
c.a = 1
print c.a
print c.__class__.a
print C.a