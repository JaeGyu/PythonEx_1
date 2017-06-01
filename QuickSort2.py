
def pation(nums):
    tmp = nums[0]
    nums[0] = nums[1]
    nums[1] = tmp

    return 1

def main():
    nums = [3,2,1]

    p = pation(nums)

    for n in nums:
        print(n)


if __name__ == "__main__":
    main()
