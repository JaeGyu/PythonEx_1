#_*_ coding: utf-8 _*_

def print_two(*args):
	arg1, arg2 = args
	print "실행인자1: %r, 실행인자2: %r" % (arg1,arg2)

def print_two_again(arg1,arg2):
	print "실행인자1: %r, 실행인자2: %r" % (arg1,arg2)

def print_one(arg1):
	print "실행인자1: %r" % arg1

def print_none():
	print "아무것도 받지 않음"

print_two("a","b")
print_two_again('c','d')
print_one('e')
print_none()
