count = 1
data  = []

print("파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]을 누르세요.")

while True:
    text = input("{} 파일에 저장할 내용을 입력 하세요: ".format(count))
    if text == "":
        break

    data.append(text+'\n')
    count += 1

with open('mydata.txt','w') as f:
    f.writelines(data)
    