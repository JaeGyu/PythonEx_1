#_*_ coding: UTF-8 _*_


list = range(1,10)

l2 = [i * 2 for i in list]

for i in l2:
    print(i)

print("-"* 70 )

l = map(lambda x: x+1, range(1,10))
for i in l:
    print(i)

print("&"*70)

l = map(lambda x,y: x+y, [3,1],[3,2,4])

for i in l:
    print(i)

