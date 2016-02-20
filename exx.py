#_*_ coding: utf-8 _*_

def needsclap(x):
	return x==2 or x==3 or x==5 or x==7

for i in range(1,101):
	one = needsclap(i%10)
	ten = needsclap(i/10)
	if one and ten: print i,"짝짝"
	elif one or ten: print i,"짝"
	else: print i

print [1,2,3] + ["ff"]
print [1,2] * 3

a = [1,2,3,4,5,6,7,8,9]
a[1] = 5
print a[-2]
print a[3:5]
print a[::-1]


birthdays = [
	("한재규", 1981, 8, 26),
	("박현규", 1981, 6,6),
	("장기호", 1980, 9, 2)
]

print birthdays

for name, year, month, day in birthdays:
	print name, year,"년", month, "월", day, "일생"
	print "%s - %s월 %s일생" % (name,month,day)

print "==========================="

formatfun = "{0} - {1}월 {2}일생".format
macro = "{0} - {1}월 {2}일생"

for name, _, month, day in birthdays:
	print formatfun(name, month, day)
	print macro.format(name, month, day)

print "4",type(4)
print "hello?", type("hello")
print "[1,2,3]", type([1,2,3])
print "(1,2,3)", type((1,2,3))
print type(formatfun)
print type(macro)
print type(birthdays)
print type(needsclap)

print "hello".upper()
print "".join(["i"," ","am"])
print "i am".split(" ")

for i in "i am a boy".split(" "):
	print i


print repr(1/5.0)
print str(1/5.0)

def names(birthdays):
	result = []
	for name,_,_,_ in birthdays:
		result.append(name)
	result.sort()
	return result

print names(birthdays)


for name in names(birthdays):
	print name

a,b,c = [1,2,3]
print a,b,c