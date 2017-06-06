"""
1
11
21
1211
111221
312211
13112221
"""
def ant(num):
    store = []
    cnt = 0
    before_element = -1

    for i in num:
        if before_element == -1:
            before_element = i
            cnt += 1
        elif before_element != i:
            store.append(cnt)
            store.append(before_element)
            before_element = i
            cnt = 1
        else:
            cnt += 1
    store.append(cnt)
    store.append(before_element)

    return store


if __name__ == "__main__":
    temp = [1]
    print(temp)

    for i in range(10):
        temp = ant(temp)
        print(temp)