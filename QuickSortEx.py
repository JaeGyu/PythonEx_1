
def sort(li):
    if len(li) > 0:
        pivot = li[-1]    
        left = []
        right = []

        for i in li[:-1]:
            if i > pivot:
                right.append(i)
            else:
                left.append(i)
        
        return sort(left) + [pivot] + sort(right)
    else:
        return li


def sort2(seq):
    if len(seq) <= 1:
        return seq

    p = seq[-1]
    left, right = [], []

    for i in seq[:-1]:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return sort2(left) + [p] + sort2(right)


def sort3(seq):
    if len(seq) <= 1:
        return seq

    p = seq[0]
    left, right = [], []

    for i in seq[1:]:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return sort3(left) + [p] + sort3(right)

def sort4(seq):
    if len(seq) <= 1:
        return seq

    p = seq[0]
    left, right = [], []

    for i in seq[1:]:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    
    return sort4(left) + [p] + sort4(right)

def patition(seq, lo, hi):
    curr_idx = lo

    for i in range(lo, hi):
        if seq[i] < seq[hi]:
            temp = seq[i]
            seq[i] = seq[curr_idx]
            seq[curr_idx] = temp
            curr_idx += 1
    
    result = curr_idx
    temp = seq[curr_idx]
    seq[curr_idx] = seq[hi]
    seq[hi] = temp
    return curr_idx 

def sort5(seq, lo, hi):
    if lo < hi:
        p = patition(seq, lo, hi)
        sort5(seq, lo, p-1)
        sort5(seq, p+1, hi)

def sort6(seq):
    if len(seq) <= 1:
        return seq

    p = seq[-1]
    l, r = [], []

    for i in seq[:-1]:
        if i < p:
            l.append(i)
        else:
            r.append(i)
    return sort6(l) + [p] + sort6(r)

def sort7(seq):
    if len(seq) < 1:
        return seq

    p = seq[0]
    l, r = [], []

    for i in seq[1:]:
        if i < p:
            l.append(i)
        else:
            r.append(i) 
    return sort7(l) + [p] + sort7(r)

def sort8(seq):

    if len(seq) <= 1:
        return seq

    p = seq[-1]
    l, r = [], []

    for i in seq[:-1]:
        if i < p:
            l.append(i)
        else:
            r.append(i)
    
    return sort8(l) + [p] + sort8(r)

def part(seq, lo, hi):
    c_i = lo

    for i in range(lo, hi):
        if seq[i] < seq[hi]:
            temp = seq[i]
            seq[i] = seq[c_i]
            seq[c_i] = temp
            c_i += 1
    
    temp = seq[c_i]
    seq[c_i] = seq[hi]
    seq[hi] = temp

    return c_i

def sort9(seq, lo, hi):
    if lo < hi:
        p = part(seq, lo, hi)
        sort9(seq, lo, p-1)
        sort9(seq, p+1, hi)

def sort10(seq):

    if len(seq) <= 1:
        return seq

    p = seq[0]
    l, r = [], []

    for i in seq[1:]:
        if i < p:
            l.append(i)
        else:
            r.append(i)
    return sort10(l) + [p] + sort10(r)


def sort11(seq):
    if len(seq) < 1:
        return seq

    p = seq[0]
    l, r = [], []

    for i in seq[1:]:
        if i < p:
            l.append(i)
        else:
            r.append(i)
    return sort11(l) + [p] + sort11(r)

def sort12(seq):
    if len(seq) < 1:
        return seq 

    p = seq[-1]
    l, r = [], []

    for i in seq[:-1]:
        if i < p:
            l.append(i)
        else:
            r.append(i)
    
    return sort12(l) + [p] + sort12(r)


def sort13(seq):

    if len(seq) < 1:
        return seq

    pivot = seq[0]
    left, right = [], []

    for i in seq[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return sort13(left) + [pivot] + sort13(right)




if __name__ == "__main__":
    li = [4,5,3,2,1]
    print(sort13(li))

