class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for i in d:
            if d[i]%2 != 0:
                return False
        return True