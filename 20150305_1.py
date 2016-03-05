#_*_ coding: utf-8 _*_

class S1:
	"Class S1"
	"Class S1"
	a=1
	"END"

print S1.a
print


S1.b=2
print S1.b
print 

print dir(S1)
del S1.b
print dir(S1)
print S1.__doc__
print S1.__module__

x = S1() # S1의 생성자를 호출하면서 객체를 만든다. 여기서 S1에관한 생성자는 디폴트 생성자이다.
print x.a

x.a = 10 # 클래스 인스턴스 x의 이름 공간에 존재하는 a에 10을 넣는다.
print x.a

print S1.a

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
print s2.stack
