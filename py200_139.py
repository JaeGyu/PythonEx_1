with open('stockcode.txt','r') as f:
    lines = f.readlines()
    for line_num,line in enumerate(lines):
        print("{} {}".format(line_num+1, line), end= "")

print()

for i,i_val in enumerate([10,11,12]):
    print("{} {}".format(i,i_val))