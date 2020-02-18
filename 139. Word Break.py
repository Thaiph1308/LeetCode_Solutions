import itertools

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]


# s = "leetcode"
# wordDict = ["leet", "code"]

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

def wordBreak(s, wordDict):
    print(len(s))
    dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
    dp[0] = True
    for i in range(len(s)):
        if dp[i]:
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    print("S[i:j]: {},\t\ti = {},j = {}".format(s[i:j],i,j))
                    dp[j] = True     
    print_info(dp)
    return dp[-1]

print(wordBreak(s,wordDict))
 