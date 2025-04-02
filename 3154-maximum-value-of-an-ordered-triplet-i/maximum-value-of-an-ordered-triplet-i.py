class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if i < j < k:
                        print((nums[i] - nums[j]) * nums[k])
                        ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans