out = open("data.out","w")

out.write("hh\n")
print("Hello World!", file=out)
print("헬로우 월드!", file=out)
print(out)
out.close()  #file을 close할때 flush가 되면서 실제로 써진다.

data = open("data.out")

for d in data:
    print(d)

data.close()

print("-" * 60)

out2 = open("data.out","a")
print("추가되는 부분입니다.",file=out2)
out2.close()

data2 = open("data.out")

for d in data2:
    print(d)

data2.close()

print("-"*60)

out3 = open("data.out","w+")
print("추가 2부분",file=out3)

out3.close()

data3 = open("data.out")

for d in data3:
    print(d)

data3.close()