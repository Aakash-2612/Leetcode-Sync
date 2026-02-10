class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            d = {
                'even': set(),
                'odd': set()
            }
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    d['even'].add(nums[j])
                else:
                    d['odd'].add(nums[j])
                # print(d)
                if len(d['even']) == len(d['odd']):
                    ans = max(ans, j - i + 1)

        return ans