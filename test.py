import itertools
def print_info(s):
    flag = True
    print(s)
    #print(len(s))
    print(type(s))
    for i in s:
        print(i)
        if flag:
            print(type(i))
            flag=False
    pass
step ='DDRR'
a = set(itertools.permutations(step, 4))
c = (itertools.permutations(step, 4))
b = list(map('->'.join,a))

print_info(a)
print_info(c)
m = 7
n = 3
#print(sorted(map(lambda x: "".join(x), set(itertools.permutations('DDDDDDRR', 8)))))