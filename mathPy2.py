try:
    file = open("emails","r")
    list = [line.split(",")[1] for line in file if line.split(",")[0] == "John"]
    print(list)
except:
    print("파일 관련 에러 발생!")