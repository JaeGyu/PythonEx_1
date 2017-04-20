try:
    file = open('names','r')

    for line in file:
        if line.startswith("John"):
            print(line, end = "")
except FileNotFoundError:
    print("파일관련 예외발생!")



