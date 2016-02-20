#_*_ coding: utf-8 _*_


L = [1,2,3]

print type(L)
print len(L)
print L[-1]
print L+L
print L*3
print (L*3)[::-1]

l2 = ['a','b']
l2[0]='c'
print l2

l3 = range(10)
print l3
print l3[::2]
print l3[::-1]
print 4 in l3

t = (1,2,3)
print len(t)
print t[0]
print t[::-1]

t = t[::-1]
print t
print t*10
print 3 in t
t= t[::-1]
print t

d = {"name":"홍길동","age":36}
print d
print d["name"]

dic = {"a":{"name":"홍길동"}}
print dic["a"]["name"]
print "name" in d

print d.keys()
print d.values()
print d.items()


print type(None)
a = None
print a

print "-"*20
a = 500
print id(a)
print id(a)
print id(a)

c = [1,2,3]
d = [1,2,3]

print c is d
print id(c)
print id(d)

print c == d

a=1
b=1
print id(a)
print id(b)
print a is b
print c[0] is a
print id(c[0])
print a == c
