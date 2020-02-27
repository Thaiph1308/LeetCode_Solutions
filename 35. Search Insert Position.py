nums = [1,3,5,6]
target = 0
def searchInsert(nums,target):
    '''
    O(n) Approach
    '''
    lower , greater = -1 , -1 
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            if nums[i] < target:
                lower = i
            if nums[i] > target:
                greater = i
        print(lower,greater,sep=" | ")
    return 0 if lower == -1 else lower + 1

'''
O(nlogn) Approach, mid = greater + lower /2
'''
print(searchInsert(nums,target))