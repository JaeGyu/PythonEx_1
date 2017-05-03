
a = 0
b = '0'
print(a)
print(bool(a))
print(bool(b))

a = [{"a":0}]
print(a)

def change(dict):
    dict["a"] = bool(dict["a"])
    return dict

#b = map(change, a)

b = map(lambda dict: bool(dict["a"]) , a)

print([l for l in b])

print((lambda x,y: x+y)(2,3))

print((lambda r: {"a":bool(r["a"])})({"a":0}))

print(bool('0'))