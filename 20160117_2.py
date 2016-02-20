#_*_ coding: utf-8 _*_

s = [1,2,3]

s.append(5)
print s
s.append({"a":100})

s.insert(3,4)
print s

s.insert(0,"abcd")
print s

s = [1,2,3,4,5]
print s.index(3)
s.append("abc")
print s
print s.index("abc")

print s.count(2)

s = [1,2,2,2,2,2,3,4,5]
print s.count(2)

s = [1,2,-1,-7,100]
s.reverse()
print s

s.sort()
print s

s = [10,20,30,40,50]
s.remove(10)
print s

s = [10,20,30,20,40,50]
s.remove(20)
print s

s.extend([60,70])
print s

s.append([60,70])
print s

s = [10,20,30,40,50]
s.append(60)
print s
print s.pop()
print s

print s.pop(0)
print s
print s.pop(1)
print s

q = [10,20,30,40,50]
q.append(60)
print q.pop(0)
print q


