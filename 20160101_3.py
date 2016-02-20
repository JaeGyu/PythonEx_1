#_*_ coding: utf-8 _*_

# 주석입니다.
import sys
print sys.version

a = 1
b = 3

if(a == 1) and \
(b == 3): # \는 연속된 줄을 이어준다. 
	print "connected lines"

c,d = 3,4
print c,d

e = 3.5; f = 5.6
print e,f

g = 5;
print g;
print e;
print f

h,i = 3,4
h,i = i,h
print h,i


aa = [1,2,3]
bb = [10,aa,20]
cc = ['x',aa, 'y']
print aa
print bb
print cc

aa[1] = 1000
print aa
print bb
print cc


