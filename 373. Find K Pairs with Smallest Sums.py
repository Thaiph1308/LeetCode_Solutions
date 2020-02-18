import itertools
import operator

nums1= [1,3,7]
nums2= [2,5,6]
k = 3
def minus(*a):
    return a[1] - a[0]
def kSmallestPairs(nums1, nums2, k):
    nums2_neg = [x*-1 for x in nums2]
    a = list(map(sum,itertools.product(nums1, nums2_neg)))
    print(a)
    print(type(a))
    for i in a:
        print(i)
        print(type(i))
    return min([abs(x) for x in a])
print(kSmallestPairs(nums1,nums2,k))    