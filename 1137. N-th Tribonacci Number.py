# n=25
# def tribonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     f1,f2,f3 = 0,1,1
#     fn = 0
#     for i in range(3,n+1):
#         fn = f1 + f2 + f3
#         f1,f2,f3 = f2,f3,fn
#     return fn
# print(tribonacci(n))
def tribonacci(n):
        f = [0,1,1]
        if n>2:
            for i in range(0,n-2):
                print(i,f[i],f[i+1],f[i+2],f)
                f.append(f[i]+ f[i+1]+ f[i+2])
                print("sau",i,f[i],f[i+1],f[i+2],f)
        return f[n]

print(tribonacci(10))