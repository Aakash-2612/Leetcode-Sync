class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        p_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                p_sum += nums[i]
            else:
                break
        
        s = set(nums)
        while p_sum in s:
            p_sum += 1
        
        return p_sum