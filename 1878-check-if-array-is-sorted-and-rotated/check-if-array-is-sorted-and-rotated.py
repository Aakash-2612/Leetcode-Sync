class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        temp = nums + nums
        l = len(nums)
        for i in range(len(nums)):
            if temp[i:i+l] == arr:
                return True
        
        return False