#_*_ coding: utf-8 _*_
import math

print """
This is 
multi lines
"""
a = "Hello workd!"

print a[1:3]

b = "abcd"
print b[::2]

c = "123456789"
print c[0:9:2]
print c[::2]

d = [1,2,3]

print d[:1]
print d[::-1]

s= ["a","b","c"]
s[1] = "B"
print s

s = "Hello World"
s = "h" + s[1:]
print s

print len(s)

print "World" in s
print "World" not in s

print math.sqrt(2)
