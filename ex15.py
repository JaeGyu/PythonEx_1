#_*_ coding: utf-8 _*_

import sys

args = sys.argv

if len(args) < 2:
	sys.exit("�����ϰ� ���� ���ϸ��� ���� ��ũ��Ʈ �ڿ� �μ��� �Է� �ϼ���.")

filename = args[1]

txt = open(filename,"r")

print "���� %r�� ����:" % filename
print txt.read()

txt.close()


print "���� �̸��� �ٽ� �Է��� �ּ���"
file_again = raw_input("> ")

txt_again = open(file_again,"r")

print txt_again.read()

txt_again.close()
