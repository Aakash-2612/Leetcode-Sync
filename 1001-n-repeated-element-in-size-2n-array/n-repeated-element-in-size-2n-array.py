class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        items = set()
        for num in nums:
            if num in items:
                return num
            else:
                items.add(num)