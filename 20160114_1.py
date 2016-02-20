#_*_ coding: utf-8 _*_


print "name = %s, age=%s" % ('han','23')

letter ="""
안녕하세요 %s님

오늘 밤 파티에 참석해 주실 수 있나요?

그럼..

이강성 드림
"""
name = "홍길동"
print letter % name
print 
names = ["한학신","정인숙","박미경"]

for name in names:
	print letter % name
	print "-" * 40
	print

print "ff%s" % 1

print "%r" % str(1)
print repr(1)
print repr('1')

print "%5d" % 123456
print "%5.2f" % 12345678.5678

print "%s %s" % ((1,2,3),3)

# print "%s" %s ((1,2))  #에러남
print "%s" % ((1,2),)
print "{}".format((1,2))
print "%s" % str((1,2))

print "%(전화번호)s -- %(이름)s" % {"이름":"한재규", "전화번호":2323}

a=[]
for n in " 1, 2   , 3,   4,  5  ".split(","):
	a+=[int(n.strip())]
print a


print " 1, 2   , 3,   4,  5  ".replace(" ","").split(",")
print "result : ",
print map(lambda x:int(x) ," 1, 2   , 3,   4,  5  ".replace(" ","").split(","))

print range(5)

print map(lambda x:x**2, range(5))


