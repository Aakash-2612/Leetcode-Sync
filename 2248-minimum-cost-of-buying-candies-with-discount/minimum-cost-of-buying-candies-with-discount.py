class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        arr = sorted(cost, reverse=True)
        count = 0
        ans = 0
        for i in arr:
            if count == 2:
                count = 0
            else:
                ans += i
                count += 1
        
        return ans