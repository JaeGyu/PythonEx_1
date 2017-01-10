import time

def corutineA():
    n = 0

    while True:
        n = (yield n)
        time.sleep(1)
        if n%10 == 3 or n%10 == 6 or n%10 == 9:
            print("A : nothing.")
        else:
            print("A : ",n)
        n += 1


def main():
    n=0
    A = corutineA()
    A.__next__()

    while True:
        n = A.send(n)
        time.sleep(1)
        if n%10 == 3 or n%10 == 6 or n%10 == 9:
            print("B : nothing.")
        else:
            print("B : ",n)
        n += 1

if __name__ == "__main__":
    main()
