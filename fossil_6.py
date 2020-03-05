a = 'bbaaabcbcc'
flag=True
for i in range(len(a)-1):
    print("het while a: {},i: {}".format(a,i))
    if (i >= len(a)-2):
        print("BREAK")
        break
    flag=True
    while flag:
        print("before replace:",a,len(a),end=" | ")
        if (a[i+1] == a[i+2]):
            #print("C",a[i],a[i+1],a[i+2])
            a = a.replace(a[i],'',2)
        if (i >= len(a)-2):
            print("BREAK")
            break
        if (a[i] == a[i+1]):
            #print("C",a[i],a[i+1],a[i+2])
            a = a.replace(a[i],'',2)    
        print("after replace:",a,len(a))
        print(i,i+1,len(a))
        if (i >= len(a)-1):
            print("BREAK")
            break
        if (a[i] != a[i+1]):
            flag = False
    print(a)
print(a)
