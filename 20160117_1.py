#_*_ coding: utf-8 _*_

l=[]
l = [1,2,"Great"]

print l[0],l[-1]
print l[1:3], l[:]
print

L = range(10)
print L[::2]
print

print l*2
print l+[3,4,5]
print len(l)
print 
print 4 in L

a= ['spam','eggs',100,1234]
a[2] = a[2] + 23
print a

a[0:2] = [1,12]
print a

a[0:2]= [1]
print a

a[0:1] = [1,2,3]
print a

a = [1,12,123,1234]
a[0:2] = []
print a


a=[123,1234]
a[1:1] = ['spam','ham']
print a

b= [123,1234]
b[1:2] = ['spam','ham']
print b

a[:0]=a
print a


a = [1,2,3,4]
del a[0]
print a

del a[1:]
print a

a = range(4)
print a
print a[::2]
print a


del a[::2]
print a


a = range(5)
del a
#print a

s = [1,2,3]
t = ['begin',s,'end']
print t

print t[1][2]


arr2 = [[1,2,3],
          [4,5,6]]
print arr2
print arr2[0][0]

arr3 = [[[1,2],
              [3,4]],[[5,6],
			              [7,8]]]
print arr3
print arr3[1][1][0]

s[1]=100
print t


print range(10)

print range(5,15)

print range(5,15,2)

for el in range(10):
	print el, 'inch=',el*2.54, 'centi'

sun,mon,tue,wed,thu,fri,sat = range(7)
print sun,mon,tue,wed,thu,fri,sat

lt = [('one',1),('two',2),('three',3)]
for t in lt:
	print 'name=',t[0],', num=',t[1]

print 

lt = [('one',1),('two',2),('three',3)]
for t in lt:
	print 'name=%s, num=%s' % t

print "{},{}".format((1,2),"l")

for t in lt:
	print 'name={},num={}'.format(t[0],t[1])

for name,num in lt:
	print name,num

ll=[1,2,3]
print type(ll)
print tuple(ll)
print ll

