
print("\t",end="")

for i in range(10):
    for j in range(0,i):
        print("*",end="")
    print("")

l = [i%2 for i in range(10)]
print(l)


