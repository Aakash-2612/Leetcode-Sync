class Solution:
    def climbStairs(self, n: int) -> int:
        def f(n, dp):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = f(n-1, dp) + f(n-2, dp)
            return dp[n]
        
        dp = [-1] * (n+1)
        return f(n, dp)