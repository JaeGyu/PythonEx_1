f = open('./sample.txt','r')
print(f.read())
print("-" * 60)
f.seek(0)
print(f.readline())
f.seek(0)
print("-" * 60)
l = f.readlines()
for i in l:
    print(i)



