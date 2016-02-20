#_*_ coding: utf-8 _*_


print divmod(5,3)

a = divmod(5,3)
print a

a,b = 5/3,5%3
print a,b

print 5//3


print 'abcd' > 'abc'
print (10,2,4) < (2,4,8)
print [1,3,2] == [1,2,3]

print (1,2,3) == (1,3,2)

L = [1,2,3, 'abc','a','z',(1,2,3),[1,2,3],{a:2},['abc']]
L.sort()
print L
