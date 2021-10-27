class Solution:
    mem = {}
    def climbStairs(self, n):

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n-1 not in self.mem:
            self.mem[n-1] = self.climbStairs(n-1)

        if n-2 not in self.mem:
            self.mem[n-2] = self.climbStairs(n-2)

        return self.mem[n-1] + self.mem[n-2]

sol = Solution()
print(sol.climbStairs(4))