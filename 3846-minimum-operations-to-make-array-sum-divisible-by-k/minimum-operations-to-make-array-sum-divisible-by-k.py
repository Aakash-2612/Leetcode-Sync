class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        if s % k == 0:
            return 0
        close = (s//k) * k
        return s - close