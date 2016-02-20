#_*_ coding: utf-8 _*_


L = [1,5,3,9,8,4,2]
L.sort()
print L

print cmp(1,2)
print cmp(2,1)
print cmp(2,2)


def mycmp(a1,a2):
	return cmp(a2,a1)

print mycmp(1,2)

L.sort(mycmp)
print L


def cmp_1(a1,a2):
	return cmp(a1[1],a2[1])

def cmp_2(a1,a2):
	return cmp(a1[2],a2[2])

L = [('lee',5,38),('kim',3,28),('jung',10,36)]
L.sort()
print 'sorted by name', L

L.sort(cmp_1)
print 'sorted by experience:',L

L.sort(cmp_2)
print 'sorted by age:',L

L=[1,6,3,8,6,2,9]
L.sort(reverse = True)
print L
L.sort(reverse = False)
print L

L=['123','34','56','2345']
L.sort()
print L

L.sort(key=int)
print L

L =[1,6,3,8,6,2,9]
newList = sorted(L)
print newList
print L

print sorted(L,mycmp)
print L

print sorted(L,reverse=True)


L=['123','34','56','2345']
print sorted(L,key=int)

L=[1,6,3,8,6,2,9]
L.reverse()
print L

L=[1,6,3,8,6,2,9]
print L
for ele in reversed(L):
	print ele+2
print
print L

print type(reversed(L))
print type(sorted(L))