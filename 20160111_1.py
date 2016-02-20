#_*_ coding: utf-8 _*_

s = 'i like programming'

print s.upper()
print s.upper().lower()
print 'I Like Programming'.swapcase()
print s.capitalize()
print s.title()

s = 'i like programming, i like swimming.'
print s.count('like')
print
print s.find('like')
print s.find('programming')
print s.find('programmin')
print s.find('programmii')
print 
print s.find('like',3)
print s.find('my')

s = 'i like programming, i like swimming.'
print s.startswith('i like')
print s.startswith('I like')
print
print s.endswith('swimming.')
print s.startswith('progr',7)

u = '    spam and ham          '
print u.strip()
print u
y = u.strip()
print y
print

print u.rstrip()
print u.lstrip()
print '            abc'.strip()
print '>>>>>><><><<<<<>>><<abc>>>><<<<><><<>>>>>'.strip('><')

p = '\t abc \t'
print p
print p.strip()

u = "spam and ham"
print u.replace("spam","spam, egg")
print u

u = " spam and ham      "
print u.split()
print u.split("and")
print

u2 = "spam and ham\tegg\ncheese"
print u2.split()

u = "spam ham\tegg\ncheese"
t = u.split()
print t
print
t2 = ":".join(t)
print t2
print
t3 = ",".join(t)
print t3
print
t4 = "\n".join(t)
print t4
print

u2 = u"스팸 햄 계란 치즈"
t2 = u2.split()
print t2
print t2[0], t2[1], t2[2], t2[3]


lines = '''first line
second line
third line'''

print type(lines)
lines2 = lines.splitlines()
print type(lines2)
print lines2
print lines.split("\n")

u = "spam and egg"
c = u.center(60)
print type(c)
print c
print u.ljust(60)
print u.rjust(60)


u = "spam and egg"
print u.center(60,"-")
print u.ljust(60,"-")
print u.rjust(60,"-")


print "1234".isdigit()
print "an".isdigit()
print "aa".isalpha()
print "dfd123".isalnum()
print "33".isalnum()
print "abc".islower()
print "AA".islower()
print "aA".islower()
print "ABC".isupper()
print "\t\r\n".isspace()
print "This Is A Title".istitle()
print "This is".istitle()


s="123"
print s.zfill(5)
print "goofy".zfill(6)



