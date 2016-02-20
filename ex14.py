#_*_ coding: utf-8 _*_

import sys

args = sys.argv

if len(args) < 2:
	sys.exit("Usage: ex14 이름")

script = args[0]
user_name = args[1]

prompt = "> "

print "안녕 %s, 나는 %s 스크립트야." % (user_name, script)
print "몇 가지 길문을 할게."
print "%s, 나를 좋아해?" % user_name
likes = raw_input(prompt)

print "%s, 어디에 살아?" % user_name
lives = raw_input(prompt)

print "무슨 종류의 컴퓨터를 갖고 있어?"
computer = raw_input(prompt)

print"""
좋아, 나를 좋아하냐는 질문에는 '%s'.
'%s'에 살아. 어딘지는 모르겠지만.
그리고 '%s' 컴퓨터를 가졌어. 멋쪄.
""" % (likes, lives, computer)

