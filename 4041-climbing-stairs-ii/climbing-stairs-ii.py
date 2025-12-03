class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def f(ind):
            if ind == 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            first = f(ind - 1) + costs[ind-1] + (1)**2
            second = float("inf")
            third = float("inf")
            if (ind - 2 >= 0):
                second = f(ind - 2) + costs[ind-1] + (2)**2
            if (ind - 3 >= 0):
                third = f(ind - 3) + costs[ind-1] + (3)**2
            dp[ind] = min(first, second, third)
            return dp[ind]
        
        dp = [-1] * (n+1)
        return f(n)