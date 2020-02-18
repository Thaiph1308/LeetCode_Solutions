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