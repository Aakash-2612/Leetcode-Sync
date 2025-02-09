class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        temp = -1
        first = True
        for index, i in enumerate(nums):
            if i == target and not first:
                temp = index
            elif i == target and first:
                ans[0] = index
                temp = index
                first = False
        
        ans[1] = temp
        return ans
        
        
