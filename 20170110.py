n=1

def func():
    global n
    print("outter n :: ",n)
    n = 2
    print(n)

def main():
    func()

if __name__ == "__main__":
    main()
