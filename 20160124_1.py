#_*_ coding: utf-8 _*_


t1 = ()
print type(t1)

t3 = 1,2,3
print type(t3)

r1 = (1)
print r1
print type(r1)
r1 = (1,)
print r1
print type(r1)


t = (1,2,3)
print t*2
print t+('aaa','bbb')
print t
print
print t[0], t[1:3]
print len(t)
print 1 in t

print range(1,3)

t= (12345,54321,'hhh')
u = t,(1,2,3,4,5)
print u

t2 = [1,2,3]
u2 = t2,(1,2,4)
print u2

t3 = {1:'ggg',2:'hhh'}
u3 = t3,(1,2,3)
print u3

x,y,z=1,2,3
print x
print y
print z

t = 1,2,'hello'
x,y,z = t





