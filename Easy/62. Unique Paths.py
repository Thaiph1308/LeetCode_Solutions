import itertools
m = 7
n = 3

def print_info(s):
    flag = True
    print(s)
    print(len(s))
    print(type(s))
    for i in s:
        print(i)
        if flag:
            print(type(i))
            flag=False
    pass

def uniquePaths(m,n):
    e = ['D']*(m-1)
    f = ['R']*(n-1)
    e = 'DDDDDD'
    f = 'RR'
    g = e+f
    print(g)
    d = list(map(list,itertools.product(g,repeat=4)))
    #print_info(g)
    print_info(d)
    #print(len(d))
    pass

uniquePaths(m,n)