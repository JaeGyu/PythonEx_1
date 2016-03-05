#_*_ coding: utf-8 _*_

class Var:
	c_mem =100 #클래스 멤버 정의
	def f(self):
		self.i_mem = 200 #인스턴스 멤버 정의 
	def g(self):
		print "-"*40
		print self.i_mem
		print self.c_mem
		print "-"*40

print Var.c_mem

v1 = Var()
print v1.c_mem
v1.f()
print v1.i_mem
	
print 
v2 = Var()
#print v2.i_mem

print
print v1.c_mem
print v2.c_mem

print
v1.c_mem = 50 #v1객체에 인스턴스 멤버 c_mem을 생성하고 50을 대입
print v1.c_mem 
print v2.c_mem #v2에 c_mem이라는 인스턴스 멤버는 없다 따라서 클래스 멤버에서 c_mem을 찾는다.

print Var.c_mem

