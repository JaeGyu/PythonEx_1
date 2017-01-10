
import re

p = re.compile("[a-z]")

m = p.match("zaa")
m2 = p.match("4")
print(m)
print(m2)

if m:
    print("매치 됨 : ", m.group())
else:
    print("매치 안됨")
    
