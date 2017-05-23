a = {'jan':1,'feb':2}
print(a)
print(type(a))

b = dict(jan=1,feb=2)
print(b)
print("abc".title())

month_names = [("a",1),("b",2)]
c = {name.title():num for name, num in month_names}
print(c)

d = {name:num for name,num in month_names if num % 2 == 0}
print(d)

months = dict(month_names)

print(months)
print(months.items())
#dict의 키와 밸류를 뒤집는다. 
e = {v:k for k,v in months.items()}
print(e)
print(e.items())

print('a' in months)
print('A' in months)
print(months['a'])

print(months.get('A')) #'A'라는 키를 찾는데 없다면 밸류를 None로 해라!
print(months.get('A',111)) #'A'라는 키를 찾는데 없다면 밸류를 111로 해라!

months.setdefault('A',111) #'A'라는 키를 찾는데 없다면 새로 등록 을 한다.
print(months['A'])

print("=" * 80)

words = open('./words').read().splitlines()
print(words)

length_count = {}

for l in map(len, words):
    if l in length_count:
        length_count[l] += 1
    else:
        length_count[l] = 1

print(length_count)
print(list(map(len,words)))

print("=" * 80)

length_count = {}

for l in map(len,words):
    length_count[l] = length_count.get(l,0) + 1

print(length_count)

by_len = {}

for w in words:
    by_len.setdefault(len(w), []).append(w)

print(by_len)

print(months.keys())
print(months.values())

