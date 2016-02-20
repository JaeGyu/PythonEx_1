#_*_ coding: utf-8 _*_

print True * 2
print False * 30

print bool(0)
print bool(1)
print bool(-1)
print bool(0.0)
print bool(0.1)

if 0 == False:
	print '참'
else:
	print '거짓'

print bool('')
print bool(' ')
print bool(None)
print bool({})
print bool([])

if 0 == True:
	print "참"
else:
	print "거짓"

print [] or ()   #  --> () 왜냐? or은 앞의 것을 평가 하고 앞의 것이 False이면 or 뒤에 것을 평가하고 그에 결과 찍는다.

print [[]] or 1 # --> [[]]를 평가 해보니 True이네 그럼 뒤에 걸 볼거 없다. or인경우에는

print not(1 or 2)
print not('' or 1)

print bool(())
print bool([])
print bool([0])
print bool([{}])

print 5 % -3
print -3 /4
print -(7/4)
print -5/3

list =  [4,{"a":"gg"},(1,2),"gg",[1,2]]
list.sort()
print list

