#_*_ coding: utf-8 _*_

class MyClass:
	def set(self, v):  #self라는 인자가 있으면 이 메서드는 인스턴스 메서드임을 나타낸다.
		self.value = v
	def get(self):
		return self.value

class Simple:
	pass

t = MyClass()
print t

t.set("hello")
print t.get()
print t.value

c = MyClass()
c.set("egg")
print c.get()
print c.value

s = Simple()

c = MyClass()
MyClass.set(c, "foo")
print MyClass.get(c)
print c.value

def set(i):
	print "set function outside function - ",i

class MyClass:
	def set(self, v):
		self.value = v
	
	def incr(self):
		set(self.value+1)
	
	def get(self):
		return self.value

c = MyClass()
c.set(1)
print c.get()

c.incr()
print c.get()

class D:
	@staticmethod
	def spam(x,y):
		print "static method:",x,y


D.spam(1,2) #인스턴스 객체 없이 클래스에서 직접 호출

print
d = D()
d.spam(1,2) #인스턴스 객체를 통해서도 호출 가능


class C:
	@classmethod
	def spam(cls, y):
		print cls, "->", y
	
print C

print
C.spam(5)

print
c = C()
c.spam(5)

print "-"*80

class D(C):  #클래스 D는 클래스 C를 상속한다.
	pass

D.spam(3)

d = D()
d.spam(3)
