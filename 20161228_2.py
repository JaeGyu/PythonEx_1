out = open("data.out","w")
out.write("hh")

print(out)

out.close()

data = open("data.out")

for d in data:
    print(d)

data.close()
