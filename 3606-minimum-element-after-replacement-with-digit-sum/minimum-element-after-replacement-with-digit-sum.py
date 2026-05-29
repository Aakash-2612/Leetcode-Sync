class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")
        for i in nums:
            s = str(i)
            a = 0
            for j in s:
                a += int(j)
            ans = min(ans, a)
        
        return ans