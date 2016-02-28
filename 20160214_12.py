
x=2

def f():
	x=1
	def g():
		print x
	g()

f()