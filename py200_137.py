f = open('stockcode.txt','r',encoding='utf8')
data = f.read()
print(data)
f.close()

with open('stockcode.txt','r', encoding='utf8') as f:
    print(f.read())