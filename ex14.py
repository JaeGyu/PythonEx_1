#_*_ coding: utf-8 _*_

import sys

args = sys.argv

if len(args) < 2:
	sys.exit("Usage: ex14 �̸�")

script = args[0]
user_name = args[1]

prompt = "> "

print "�ȳ� %s, ���� %s ��ũ��Ʈ��." % (user_name, script)
print "�� ���� �湮�� �Ұ�."
print "%s, ���� ������?" % user_name
likes = raw_input(prompt)

print "%s, ��� ���?" % user_name
lives = raw_input(prompt)

print "���� ������ ��ǻ�͸� ���� �־�?"
computer = raw_input(prompt)

print"""
����, ���� �����ϳĴ� �������� '%s'.
'%s'�� ���. ������� �𸣰�����.
�׸��� '%s' ��ǻ�͸� ������. ����.
""" % (likes, lives, computer)

