
def swap(l, s, t):
    temp = l[s]
    l[s] = l[t]
    l[t] = temp

def patition(p, lo, hi):
    current_idx = lo

    for i in range(lo,hi):
        if l[i] < l[hi]:
            swap(l, i, current_idx)
            current_idx += 1

    swap(l, hi, current_idx)
    
    return current_idx


def qsort(l, lo, hi):
    if lo < hi:
        p = patition(l, lo, hi)
        qsort(l, lo, p-1)
        qsort(l, p+1, hi)
        

if __name__ == "__main__":
    l = [5,4,3,2,1]
    print(l)
    qsort(l, 0, 4)
    print(l)