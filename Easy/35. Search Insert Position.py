nums = [1,3,5,7]
target = 2
# def searchInsert(nums,target):
#     '''
#     O(n) Approach
#     '''
#     lower , greater = -1 , -1 
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#         else:
#             if nums[i] < target:
#                 lower = i
#             if nums[i] > target:
#                 greater = i
#         print(lower,greater,sep=" | ")
#     return 0 if lower == -1 else lower + 1

# '''
# O(logn) Approach, mid = greater + lower /2
# '''

def searchInsert(nums,target):  
    low = 0
    high = len(nums)-1
    mid = 0
    while low <= high:
        print(low,mid,high)
        mid = (low + high)//2
        if (nums[mid] == target):
            return mid
        if (nums[mid] < target):
            low = mid + 1
        if (nums[mid] > target):
            high = mid - 1
    return low
print(searchInsert(nums,target))