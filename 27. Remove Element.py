nums = [0,1,2,2,2,2,2,3,0,4,2]
val = 2

def remove_elements(nums,val):
    i = 0
    while (i < len(nums)):
        if (nums[i] == val):
            print(nums,i,val)
            nums.pop(i)
        else:
            i = i + 1
    print(len(nums))
    return len(nums)
remove_elements(nums,val)