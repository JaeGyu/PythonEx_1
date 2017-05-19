def toFibo(n):
    temp = {}

    def fibo(n):
        if n in temp.keys():
            return temp[n]

        if n < 2:
            temp[n] = 1
            return 1

        temp[n] = fibo(n-1) + fibo(n-2)
        return temp[n]

    for i in range(n):
        print(i," : ",fibo(i))

if __name__ == "__main__":
    toFibo(100)