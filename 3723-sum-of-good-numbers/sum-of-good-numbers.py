class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                if nums[i-k] < nums[i] and nums[i+k] < nums[i]:
                    s += nums[i]
            else:
                if i - k >= 0:
                    if nums[i-k] < nums[i]:
                        s += nums[i]
                        # print(nums[i])
                if i + k < len(nums):  
                    if nums[i+k] < nums[i]:
                        s += nums[i]
                        # print(nums[i])
        
        return s