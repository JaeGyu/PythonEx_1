import random as rnd

def quick_sort(list, lo, hi):
    if lo < hi:
        p = patition(list, lo, hi)
        quick_sort(list, lo, p-1)
        quick_sort(list, p+1, hi)

def swap(list, source, target):
    tmp = list[source]
    list[source] = list[target]
    list[target] = tmp

def patition(list, lo, hi):

    pivot_num = list[hi]
    current_idx = lo

    for i in range(lo,hi):
        if list[i] < pivot_num:
            swap(list, i, current_idx)
            current_idx += 1
    
    swap(list, hi, current_idx)

    return current_idx

def main():
    nums = rnd.sample(range(10), 10)
    print("before sort : ",nums)

    quick_sort(nums, 0, 9)
    print("after  sort : ",nums)

if __name__ == "__main__":
    main()