import collections

nums = [1,2]
k = 5

# nums = [1,2,3]
# k = 2

# nums = [1]
# k = 1

# nums = [1,2,3,4,5,6,7]
# k = 3

# nums_2 = [-1,-100,3,99]
# k_2 = 2

# num_3 = [1]
# k_3 = 1

# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Approach 1, Time complexity O(n), Auxiliary space O(n), NOT INPLACE 
# left = 0
# right = len(nums) -1 
# temp = 0
# dequeue = collections.deque(nums)
# print(dequeue)
# for i in range(0,k):
#     temp = dequeue[right]
#     dequeue.pop()
#     dequeue.appendleft(temp)

# Approach 2, In Place
number_of_step = k % len(nums)
for i in range(0,number_of_step):
    print(number_of_step)
    print(nums[len(nums) - number_of_step : len(nums)] + nums[ : len(nums) - number_of_step])