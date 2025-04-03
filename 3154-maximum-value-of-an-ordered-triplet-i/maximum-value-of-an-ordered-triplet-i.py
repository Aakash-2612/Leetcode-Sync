class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]
        for j in range(1, len(nums)):
            if left < nums[j]:
                left = nums[j]
                continue
            for k in range(j+1, len(nums)):
                ans = max(ans, (left - nums[j]) * nums[k])
        return ans