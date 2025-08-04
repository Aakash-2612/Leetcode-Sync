class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        cur_max = 0
        ans = 0
        for i in range(len(weight)):
            cur_max = max(weight[i], cur_max)
            if weight[i] < cur_max:
                ans += 1
                cur_max = 0
            
        return ans