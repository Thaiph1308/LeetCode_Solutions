# nums = [0,0,0,1,12,0,0,0]

nums = [0,1,0,3,12]

def move_zeroes(nums):
    i = 0
    for j in nums:
        if (j != 0):
            nums[i] = j
            i = i + 1
    nums[i:] = [0]*(len(nums)-i)
move_zeroes(nums)

################################################################

pos = 0
for i in range(len(nums)):
    if (nums[i] != 0):
        nums[pos] , nums[i] = nums[i], nums[pos]
        pos += 1
