# nums = [2,0,2,1,1,0]
nums = [1,1]
# nums = [2,0,1]
# nums = [2,2,1,1,2,0,1]
# nums = [1,1,1,1,1,1,1,1,1,1,2,0,2]

# start = 0
# end = len(nums) - 1
# mid = 0 
# while mid <= end:
#     print("==",start,mid, end, nums[start], nums[mid], nums[end], nums)
#     if (nums[start] == 0):
#         start += 1
#         mid += 1
#         print("start = 0")
#     elif (nums[start] == 2):
#         nums[start] , nums[end] = nums[end] , nums[start]
#         end = end - 1
#     elif (nums[mid] == 1 and mid == end):
#         end = end -1    
#     elif (nums[mid] == 1):
#         mid += 1
#     elif (nums[mid] != 1):
#         nums[start] , nums[mid] = nums[mid] , nums[start]
#         print("start = 2")

#     print("=>",start,mid, end, nums[start], nums[mid], nums[end], nums)


### Result

red = 0
white = 0 
blue = len(nums) - 1
while white <= blue:
    print("==",red,white, blue, nums[red], nums[white], nums[blue], nums)
    if nums[white] == 0:
        nums[red], nums[white] = nums[white], nums[red]
        white += 1
        red += 1
    elif nums[white] == 1:
        white += 1
    elif nums[white] == 2:
        nums[white], nums[blue] = nums[blue], nums[white]
        blue -= 1
    # if (nums[white] == 0):
    #     nums[red] , nums[white] = nums[white] , nums[red]
    #     red += 1
    #     white += 1
    # elif (nums[white] == 1):
    #     white += 1
    # else:
    #     nums[blue] , nums[white] = nums[white] , nums[blue]
    #     blue = blue -1
    print("=>",red,white, blue, nums[red], nums[white], nums[blue], nums)
