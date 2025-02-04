class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_sum = nums[0]
        for r in range(1, len(nums)):
            if nums[r-1] < nums[r]:
                cur_sum += nums[r]
            else:
                ans = max(ans, cur_sum)
                cur_sum = nums[r]
        
        ans = max(ans, cur_sum)
        return ans