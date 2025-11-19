class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        val = original
        if val not in nums:
            return val

        return self.findFinalValue(nums, val*2)
