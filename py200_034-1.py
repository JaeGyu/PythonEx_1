from time import sleep

for i in range(100):
    msg = "\r진행률ff %d%%" % (i + 1)
    print("" * len(msg), end="")
    print(msg, end="")
    sleep(0.01)
    
print()
for i in range(100):
    print("result : %d" % (i+1),end="")
    sleep(0.1)
