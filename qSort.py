
def patition(l, s, e):
    current_idx = s

    for i in range(s,e):
        if l[i] < l[e]:
            temp = l[current_idx]
            l[current_idx] = l[i]
            l[i] = temp
            current_idx += 1
    
    temp = l[current_idx]
    l[current_idx] = l[e]
    l[e] = temp
    return current_idx


def qsort(l, s, e):
    if s < e:
        p = patition(l,s,e)
        qsort(l, s, p-1)
        qsort(l, p+1, e)

if __name__ == "__main__":
    l = [5,4,3,2,1]
    print(l)
    qsort(l,0,4)
    print(l)