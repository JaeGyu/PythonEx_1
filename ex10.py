#_*_ coding: utf-8 _*_

tabby_cat = "\t난 탭이 됨."
persian_cat = "나는 \\고\\양이."

fat_cat = """
할 일 목록:
\t\t\t* 고양이 밥
\t\t\t* 물고기
\t\t\t* 개박하\n\t\t\t* 오리새
\a\a\b\b\b\b\b\f\n\r\v
"""

print tabby_cat
print persian_cat
print fat_cat

print '''
asdf
asf
1234567890
'''

print "%r" % "\a"

'''
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i, 
'''