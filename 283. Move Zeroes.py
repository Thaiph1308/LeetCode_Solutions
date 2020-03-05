nums = [0,0,0,1,12,0,0,0]

def move_zeroes(nums):
    i = 0
    for j in nums:
        if (j != 0):
            nums[i] = j
            i = i + 1
    nums[2:] = [0]*(len(nums)-i)
move_zeroes(nums)