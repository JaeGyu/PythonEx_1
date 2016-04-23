#_*_ coding: utf-8 _*_

import os

print os.getcwd()

s="""Its power: Python developers typically reoport
ther are able to develop applications in a half
to a tenth the amount
입니다."""

f=open('t.txt','w')
f.write(s)
f.close()
