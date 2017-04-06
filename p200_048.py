f = open("./py200_sample.txt", "w")

f.write("abcd")
f.close()

r = open("./py200_sample.txt", "rb")

print("-" * 60)
print(r.readline())

r.close()
