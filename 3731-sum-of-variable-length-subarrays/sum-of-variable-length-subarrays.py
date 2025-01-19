class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        arr = []
        for ind, i in enumerate(nums):
            start = max(0, ind - i)
            arr.append(sum(nums[start:ind+1]))
        
        return sum(arr)