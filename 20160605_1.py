#_*_ coding: utf-8 _*_


class S1:
	"Class S1"
	"문자열!!"
	a = 1 #a라는 변수는 S1이라는 클래스의 이름공간에 존재한다.
	c = "문자열 입니다."

print S1.a
print 

S1.b = 2 #클래스 이름 공간에 새로운 이름의 생성
print S1.b
print

print dir(S1) #S1에 포함된 이름들을 리스트로 반환
del S1.b #이름 공간 S1에서 b삭제
print dir(S1)

print S1.__doc__  #class 안에 문자열이 있다면 __doc__에 할달 된다.
print S1.__module__

x = S1() #S1이 가지고 있는 생성자를 호출 한다. 여기선 눈에 안보이는 디폴트 생성자가 호출 된다.

print x.a #x라는 이름공간에 a라는 변수는 없다 따라서 S1이름공간의 a 변수 내용이 출력된다.

x.a = 10  #x라는 인스턴스의이름공간에 라는 변수를 생성하고 10을 할당한다.
print x.a 

print S1.a
print "\n"*2

y=S1()
y.a = 300
print y.a
print x.a
print S1.a


class Simple:
	pass

s1 = Simple()
s2 = Simple()

s1.stack = []
s1.stack.append(1)
s1.stack.append(2)
s1.stack.append(3)

print s1.stack
print s1.stack.pop()
print s1.stack.pop()
print
print s1.stack
#print s2.stack #s2에는 stack을 정의한 적이 없다. 에러남