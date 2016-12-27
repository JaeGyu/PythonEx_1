import os

if not(os.path.exists("sampleForFile.txt")):
    print("존재안함")
else:
    print("존재함")

f = open("sampleForFile.txt")

for data in f:
    try:
        (role, line_spoken) = data.split(":")
        print(role,line_spoken,end="")
    except ValueError:
        print("오류군!")
print()