class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            d = {}
            count = 0
            for j in range(i, len(nums)):
                if nums[j] not in d:
                    count += 1
                    d[nums[j]] = 1
                else:
                    d[nums[j]] += 1
                ans += count**2
                # print(count**2)
        
        return ans