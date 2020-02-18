import itertools
def print_info(s):
    flag = True
    print(s)
    print(type(s))
    for i in s:
        print(i)
        if flag:
            print(type(i))
            flag=False
    pass
nums = [1,2,3]

def permute(nums):
    a = list(map(list,itertools.permutations(nums)))
    print_info(a)
    pass

permute(nums)