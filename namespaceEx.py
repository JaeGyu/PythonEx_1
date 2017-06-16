def foo():
    global x
    x = 20
    y = 10
    print("locals : ", locals()) #지역 범위의 네임스페이스를 가져온다.


if __name__ == "__main__":
    foo()
    print(x)
    print("globals : ",locals()) #전역 범위의 네임스페이스를 가져온다.