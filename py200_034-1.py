from time import sleep

#print에서 end=""가 아마 \n을 없애 주는 기능인거 같다

for i in range(100):
    msg = "\r진행률ff %d%%" % (i + 1)
    print("" * len(msg), end="")
    print(msg, end="")
    sleep(0.01)
    
print()
for i in range(100):
    print("\rresult : %d" % (i+1),end="&&")
    sleep(0.1)
