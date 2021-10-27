class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_s=[0]*256
            count_t=[0]*256
            for s_i,t_i in zip(s,t):
                count_s[ord(s_i)] += 1
                count_t[ord(t_i)] += 1
            for i in range(256):
                if count_s[i] != count_t[i]:
                    return False
            return True