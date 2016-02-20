#_*_ coding: utf-8 _*_
import sys
import math

a = 23
b = 023
c = 0x23

print type(a),type(b),type(c)
print a,b,c

print sys.maxint

d = 1.2
e = 3.5e3
f = -0.2e-4
print type(d),type(e),type(f)
print d,e,f

g = 123456789098765432123456789l
print type(g)

print g * g

h = 12345678909876543212345
print h
print type(h)

print abs(-3)
print int(3.141592)
print int(-3.14)
print float(3)
print complex(3.4,5)
print complex(6)
print long(3)
print float("123.23")
print complex(float("3.4"),5)
print divmod(5, 2)
print pow(2.3, 3.5)
print divmod(5,2)[1]

print math.pi
print math.sin(1)
print math.sqrt(2)