class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size, res = 0, 0
        cur_max = 0

        for i in nums:
            if i > cur_max:
                cur_max = i
                size = 1
                res = 0
            elif i == cur_max:
                size += 1
            else:
                size = 0
            res = max(res, size)

        return res