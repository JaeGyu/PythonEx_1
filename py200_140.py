text = input("파일에 저장할 내용을 입력 하세요!")

with open("mydata.txt",'w') as f:
    f.write(text)

with open("mydata.txt",'r') as f:
    print(f.read())