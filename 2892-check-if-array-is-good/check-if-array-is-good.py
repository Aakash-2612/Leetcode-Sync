class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) != m+1:
            return False
        d = Counter(nums)
        for i in range(1, m+1):
            if i != m:
                if d[i] != 1:
                    return False
            else:
                if d[i] != 2:
                    return False
        
        return True