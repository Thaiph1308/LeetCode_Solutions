version = [False,False,False,False,True,True,True]

def isBadVersion(n):
    return version[n]

def firstBadVersion(n):
    low = 0
    high = n + 1
    while low <= high:
        mid = low + (high - low) // 2
        # print(mid)
        if mid > 1 and isBadVersion(mid - 1):
            high = mid - 1
        elif isBadVersion(mid):
            return mid
        else:
            low = mid + 1
print(firstBadVersion(len(version)))