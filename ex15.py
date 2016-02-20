#_*_ coding: utf-8 _*_

import sys

args = sys.argv

if len(args) < 2:
	sys.exit("오픈하고 싶은 파일명을 실행 스크립트 뒤에 인수로 입력 하세요.")

filename = args[1]

txt = open(filename,"r")

print "파일 %r의 내용:" % filename
print txt.read()

txt.close()


print "파일 이름을 다시 입력해 주세요"
file_again = raw_input("> ")

txt_again = open(file_again,"r")

print txt_again.read()

txt_again.close()
