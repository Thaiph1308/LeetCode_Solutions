s = "Let's take LeetCode contest"
a = []
c = ""

word = 0
for i,char in enumerate(s):
    if (char == ' '):
        print(word,i,char)
        print(s[word:i][::-1])
        a.append(s[word:i][::-1])
        c += s[word:i][::-1] + " " 
        word = i + 1
    if (i == len(s)-1):
        print(s[word:i+1])
        a.append(s[word:i+1][::-1])
        c += s[word:i+1][::-1]
print(' '.join(a))
print(c)

