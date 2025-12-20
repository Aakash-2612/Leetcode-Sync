class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        index = None
        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                index = i
                break
        
        if index == None:
            return 0
        else:
            index += 1
            return math.ceil(index/3)