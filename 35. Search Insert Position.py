nums = [1,2,3,4,5,6,7,8,9,10,11,14,16,18,19,22,31,38,44,66,99]
target = 14
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
    mid = int((low + high)/2)
    i = 0
    while i < len(nums):
        if (nums[mid] == target):
            return True
        if (nums[mid] < target):
            high = int((mid + high)/2) 
        if (nums[mid] > target):
            low = int((low+mid)/2) , low
        i = i+1

print(searchInsert(nums,target))