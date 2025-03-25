class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        l = 0
        ans = 0
        d = {key : 0 for key in nums}
        for r in range(len(nums)):
            d[nums[r]] += 1
            cur_sum += nums[r]
            if d[nums[r]] > 1:
                while d[nums[r]] != 1:
                    d[nums[l]] -= 1
                    cur_sum -= nums[l]
                    l += 1
            else:
                if (r-l+1) == k:
                    ans = max(ans, cur_sum)
                    d[nums[l]] -= 1
                    cur_sum -= nums[l]
                    l += 1
            
        return ans