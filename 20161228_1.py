man = []
woman = []

data = open("sketch.txt")

for each in data:
    (a,b) = each.split(":",1)
    b = b.strip()

    if a == "man":
        man.append(b)
    elif a == "woman":
        woman.append(b)

print(man)
print(woman)