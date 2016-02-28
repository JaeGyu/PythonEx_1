#-*- coding: utf-8 -*-

#g,h는 전역 변수
g = 10
h = 5

def f(a): # a는 지역 변수 
	h=a+10 # h는 지역, 새로 l-value로 정의했음
	b=h+a+g # b도 지역, g는 r-value이므로 기존값을 참조 - 전역 변수 
	return b

#아래의 print문은 전역 영역에 존재한다.
print f(h) #함수 호출시에 사용되는 변수는 해당 위치의 스코프에서 값을 찾음 - 전역 변수
print h #전역 변수 h는 변함 없음 