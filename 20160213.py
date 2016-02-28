#-*- coding: utf-8 -*-

print "20160213 프로그램입니다."

def hap(a,b):
	return a+b

print hap(1,2)

print "Using lamda : ",(lambda x,y:x+y)(10,20)

a = hap

print a(2,2)

def sumOfTuple(a):
	return a[0]+a[1]

b = sumOfTuple

print map(b,[(2,1),(2,2)])
print map(lambda a: a[0]+a[1],[(3,3),(4,4)])
print map(lambda a: ("This is result : %s" % (a)),["aa"])
print reduce(lambda x,y: x+y,[1,2,3,4,5,6,7,8,9,10])
print filter(lambda x: x<5,[1,2,3,4,5,6,7,8,9])

'''
 람다와 리듀스등을 가지고 피보나치 만들어 볼 것 
'''
print reduce(lambda x,y: x+y , [1,1])

