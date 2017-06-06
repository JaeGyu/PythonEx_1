"""
개미수열
1
11
12
1121
122111
112213
12221131
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
            store.append(before_element)
            store.append(cnt)
            before_element = i
            cnt = 1
        else:
            cnt += 1
    
    store.append(before_element)
    store.append(cnt)

    return store

if __name__ == "__main__":
    temp = [1]
    print(temp)
    for i in range(10):
        temp = ant(temp)
        print(temp)
    