class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            if (nums[0] + nums[1]) % 2 == 0:
                return False
        for i in range(1, len(nums)-1):
            if (nums[i-1] + nums[i]) % 2 == 0 or (nums[i+1] + nums[i]) % 2 == 0:
                return False
            
        return True