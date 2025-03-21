class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(prices)):
            if not stack:
                stack.append(prices[i])
            if stack and prices[i] < stack[-1]:
                stack.append(prices[i])
            if stack and prices[i] > stack[-1]:
                ans = max(ans, prices[i]-stack[-1]) 
        
        return ans