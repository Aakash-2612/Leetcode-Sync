class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        m = max(nums) + k + 1
        s = set(nums)
        ans = 0
        for i in range(1, m):
            if i % k == 0 and i not in s:
                ans = i
                break

        return ans