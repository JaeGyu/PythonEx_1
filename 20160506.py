#_*_ coding: utf-8 _*_

import os

#현재 경로를 표시 한다.
print os.getcwd()

s="""Its power: Python developers typically report
they are able to develop applications in a half
to a tenth the amount of time it takes them to do
the same work in such languages as C."""

f=open('t.txt','w')
f.write(s)
f.close()

#file보다 open을 더 추천
f=file('t.txt')
print f.read()
f.close()

print "-"*60

#이 방법이 제일 좋다
f=open('t.txt','r')
for line in f:
	print line

print "-"*60

f=open('t.txt','r')

line=f.readline()
while line:
	print line,
	line = f.readline()

print 
print "-"*60

#아래의 방법은 파일 크기가 클경우 라인을 저장하는 리스트의
#크기가 메모리를 초과 할 수 있다.
f=open('t.txt','r')
lines = f.readlines()
print lines

for line in lines:
	print line

print "-"*60

#아래는 필요할 때마다 한 라인씩 읽어 들인다
#메모리 절약면에 있어서 좋다.
f=open('t.txt','r')
for line in f.xreadlines():
	print line,
print 

print "-"*60



