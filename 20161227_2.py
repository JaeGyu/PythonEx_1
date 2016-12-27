#_*_ coding: UTF-8 _*_
import os

print(os.getcwd())

f = open("sampleForFile.txt")
print(f.readline(),end="")
print(f.readline())
f.seek(0)
for data in f:
    print(data,end="")
f.close()