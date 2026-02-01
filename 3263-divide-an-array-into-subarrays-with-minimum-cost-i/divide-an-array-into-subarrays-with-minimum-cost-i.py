class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = nums[0]
        arr = sorted(nums[1:])
        s += arr[0] + arr[1]
        return s