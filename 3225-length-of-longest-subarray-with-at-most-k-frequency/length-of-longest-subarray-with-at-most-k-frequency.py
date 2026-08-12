class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        l = 0
        r = 0
        count = 0
        while r < len(nums):
            if nums[r] not in d:
                d[nums[r]] = 1
            else:
                d[nums[r]] += 1
                while d[nums[r]] > k:
                    if d[nums[l]] > 0:
                        d[nums[l]] -= 1
                    l += 1
            count = max(count, (r-l+1))
            r += 1
        
        return count
            