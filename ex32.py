#_*_ coding: utf-8 _*_

the_count = [1,2,3,4,5]
fruits = ["사과","귤","배","살구"]
change = [1,'십원',2,'백원',3,'오백원']

for number in the_count:
	print "이 수는 %d" % number

for fruit in fruits:
	print "과일 종류: %s" % fruit

for i in change:
	print "받은 잔돈 %s" % change

elements = []

for i in range(0,6):
	print "List에 %d 숫자를 더합니다." % i
	elements.append(i)

for i in elements:
	print "원소는 %d" % i



