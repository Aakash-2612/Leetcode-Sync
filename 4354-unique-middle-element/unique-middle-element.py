class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        d = Counter(nums)
        m = (len(nums) - 1)//2
        if d[nums[m]] == 1:
            return True
        else:
            return False