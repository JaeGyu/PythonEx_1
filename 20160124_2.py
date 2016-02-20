#_*_ coding: utf-8 _*_

a = set([1,2,3])

print type(a)
print a

a = set((1,2,2,2,2,2,1))

print a

c = set({'a':1,'b':2})
print c

c = set({'a':1,'b':2}.values())
print c

B = set([4,5,6,10,20,30]) 
C = set([10,20,30])

print C.issubset(B)
print C <= B
print B.issuperset(C)
print B >= C
print


A = set([1,2,3,4,5,6,7,8,9])
B = set([4,5,6,10,20,30])

print A.union(B)
print A | B
print A 
print

print A.intersection(B)
print A & B
print A
print 

print A.difference(B)
print A - B
print A
print 

print A.symmetric_difference(B)
print A ^ B
print A
print 

A = set([1,2,3,4,5,6,7,8,9])
B = A.copy()
print B
print 

print A == B
print A is B

print list(A)
print tuple(A)

for ele in A:
	print ele,

print 

A = set([1,2,3,4])
B = set([3,4,5,6])

A.update(B)
print A

A.intersection_update([4,5,6,7,8])
print A

A.difference_update([6,7,8])
print A

A.symmetric_difference_update([5,6,7])
print A

A.add(8)
print A

A.remove(8)
print A

A.discard(11)
print A

print '-'*60

A = set([1,2,3,4,5])

A.pop()
print A

A.pop()
print A

A= set([1,2,3,4,5])
A.clear()
print A


