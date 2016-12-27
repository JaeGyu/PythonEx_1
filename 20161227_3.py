
def ant(num):
    result = []
    temp = -100
    cnt = 0

    for i in num:
        if i != temp:
            temp = i
            result.append(cnt)
            result.append(i)
            cnt = 0
        cnt += 1
    
    result.append(cnt)
    return result[1:]


def main():
    print("[1]")
    l = [1]
    for i in range(1,11):
        l = ant(l)
        print(l)


if __name__ == "__main__":
    main()