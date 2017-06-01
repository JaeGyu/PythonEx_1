def quick(nums, lo,hi):
    if lo < hi:
        p = pation(nums,lo,hi)
        quick(nums,lo,p-1)
        quick(nums,p+1,hi)

def pation(nums,lo,hi):
    pivotNum = nums[len(nums)-1]
    currentIdx = lo

    for i in range(lo,hi):
        if pivotNum > nums[i]:
            tmp = nums[i]
            nums[i] = nums[currentIdx]
            nums[currentIdx] = tmp
            currentIdx+=1
    
    tmp = nums[hi]
    nums[hi] = nums[currentIdx]
    nums[currentIdx] = tmp
    return currentIdx

def main():
    nums = [8,4,1,2,5,7,3]

    quick(nums,0,len(nums)-1)

    for n in nums:
        print(n)

if __name__ == "__main__":
    main()