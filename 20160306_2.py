#_*_ coding: utf-8 _*_

class Student:
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name


s1 = Student()
s1.setName("tina")

s2 = Student()
s2.setName("tom")

members = []
members.append(s1)
members.append(s2)

for member in members:
	print member.getName()