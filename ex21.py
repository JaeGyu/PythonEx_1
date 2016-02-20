#_*_ coding: utf-8 _*_

def add(a,b):
	print "µ¡¼À %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "»¬¼À %d - %d" % (a,b)
	return a-b

def multiply(a,b):
	print "°ö¼À %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "³ª´°¼À %d / %d " % (a,b)
	return a/b

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100,2)

print age
print height
print weight
print iq

print "¹®Á¦°¡ ÀÖ¾î¿ä."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "°á°ú:", what, "¼ÕÀ¸·Î °è»ê ÇÒ ¼ö ÀÖ³ª¿ä?"

