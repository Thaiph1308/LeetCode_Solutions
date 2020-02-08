s = "dvvvvvvvvvdf"
s2= "abba"
def length_of_longestSubString(s):
    _max = 0 
    _start = 0
    _dict = {}
    for i,char in enumerate(s):
        print(s[i])
        if (char in _dict):
            _max = max(i-_start,_max)
            print("_max",_max)
            _start = max(_dict[char]+1,_start)
            print("_start = {} dict_[char]+1_value = {}".format(_start,_dict[char]+1))
        _dict[s[i]] = i
    print(_dict)
    print(_max,_start)
    return max(_max,len(s)-_start)
print(length_of_longestSubString(s))