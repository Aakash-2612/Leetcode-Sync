class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                count += 1
                nums.pop(i)

        nums = nums + [0]*count
        return nums