#_*_ coding: utf-8 _*_


class S1:
	a = 1 #a라는 변수는 S1이라는 클래스의 이름공간에 존재한다.

print S1.a
print 

S1.b = 2 #클래스 이름 공간에 새로운 이름의 생성
print S1.b
print

print dir(S1) #S1에 포함된 이름들을 리스트로 반환
del S1.b #이름 공간 S1에서 b삭제
print dir(S1)