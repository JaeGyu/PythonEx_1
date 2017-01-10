
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

p = re.compile("[abc]")
print(p.match("a"))
print(p.match("before"))
print(p.match("dude"))

print("-" * 60)
p = re.compile("[1-3]")
print(p.match("aa"))
print(p.match("345"))
print("-" * 60)

p = re.compile("[^0-9]")
print(p.match("123"))
print(p.match("for"))
print("-"*60)

p=re.compile("[\d]") #숫자
print(p.match("123"))
print("-"*60)

p = re.compile("[\D]") #숫자가 아닌거
print(p.match("123"))
print("-"*60)

p = re.compile("a.b")
print(p.match("a123b"))
print("-"*60)

p = re.compile("a.b")
print(p.match("asbc"))
print("-"*60)

