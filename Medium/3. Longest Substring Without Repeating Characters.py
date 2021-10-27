# s = "abcabcbb"
# s = "pwwkew"
s  = "a"
# s = "aab"
# s = "dvdf"

# longest = 0
# output = 0
# largest = ''
# for i in range(len(s)):
#     print(s[i])
#     if (s[i] in largest):
#         largest = s[i]
#     else:
#         largest = largest + s[i]
#         output = len(largest)
#         longest = output if output > longest else longest
#         print(output, longest)

#### Brute Force O(N^2), should be Time Limit Exceeded
sLength = 0
def check(substring):
    stack = ""
    cur = 0
    for i in range(len(substring)):
        if (substring[i] in stack):
            return cur
        else:
            cur += 1
            stack = stack + substring[i]
    return cur

for i in range(len(s) + 1):
    for j in range (i + 1, len(s) + 1):
        sLength = sLength if sLength > check(s[i:j]) else check(s[i:j])

#### Sliding window
