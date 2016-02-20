#_*_ coding: utf-8 _*_

import urlparse 

print "df"
print map(lambda x: x+1,[1,2,3,4,5])
print filter(lambda x: x%2,[1,2,3,4,5,6,7,8,9])
print reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10])

result = urlparse.urlparse("http://www.naver.com");
print result


def returnTest():
	return

returnTest()

