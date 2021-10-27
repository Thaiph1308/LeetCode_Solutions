# class Solution:
#     def fib(self, N: int) -> int:
#         a,b = 0,1
#         c = 0
#         for i in range(N):
#             c = a + b
#             a,b = c,a
#         return c

'''
O(1) way
def fib(self, N):
	golden_ratio = (1 + 5 ** 0.5) / 2
	return int((golden_ratio ** N + 1) / 5 ** 0.5)
'''

'''
Smart Way
'''
# def fib(n):
#     if n>1:
#         f = [0,1]
#         for i in range(2,n+1):
#             print(i,f[i-1],f[i-2],f,end="")
#             f.append(f[i-1] + f[i-2])
#             print(">>>>>>>>>>",i,f[i],f[i-1],f)
#         return f[n]
# print(fib(4))

class Solution:
    f =[0,1]
    def fib(self, N: int) -> int:
        if N>1:
            for i in range(2,N+1):
                print(i,self.f[i-1],self.f[i-2],self.f,end="")
                self.f.append(self.f[i-1] + self.f[i-2])
                print(">>>>>>>>>>>>",i,self.f[i-1],self.f[i-2],self.f)
            return self.f[N]

sol = Solution()
print(sol.fib(3))