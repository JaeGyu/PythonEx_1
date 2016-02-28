#-*- coding:utf-8 -*-

x = 10

def f():
	a=1
	b=2

f.c=1
print f.c #함수 외부에서 지정한 변수는 호출이 가능함
print 
print f.a #애당초부터 함수 안에 정의된 지역변수는 외부에서 호출 불가능 함 