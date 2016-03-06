#_*_ coding: utf-8 _*_

class Student:
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name


s1 = Student()
s1.setName("tina")
print s1.getName()