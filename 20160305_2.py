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
	def spam(x,y):
		print "static method:",x,y
