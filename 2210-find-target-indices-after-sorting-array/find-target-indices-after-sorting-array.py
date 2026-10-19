class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        
        return ans