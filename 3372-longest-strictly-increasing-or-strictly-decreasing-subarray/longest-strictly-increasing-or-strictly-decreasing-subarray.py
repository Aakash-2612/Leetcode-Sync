class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        ind = 0
        first = 0
        second = 0
        while r < len(nums):
            if nums[ind] >= nums[r]:
                first = max(first, r-l)
                l = r
                r += 1
                ind += 1
            else:
                r += 1
                ind += 1
        if first < (r-l):
            first = r-l
        # print(first)
        l = 0
        r = 1
        ind = 0
        while r < len(nums):
            if nums[ind] <= nums[r]:
                second = max(second, r-l)
                l = r
                r += 1
                ind += 1
            else:
                r += 1
                ind += 1
        if second < (r - l):
            second = r - l
        # print(second)

        return max(first, second)