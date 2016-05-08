#_*_ coding: utf-8 _*_

import hashlib
import gzip
import urllib2

f = open('t.txt','r')

for line in f:
	print line,
print

print "-"*60

print hashlib.md5("python").hexdigest()

f = gzip.open('gzip.txt.gz','wb')
f.write("Hello World.\n")
f.close()

response = urllib2.urlopen("http://www.google.com")
data = response.read()
print data






