class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        OFFSET = 50
        freq = [0] * 101
        ans = []
        for i in range(k):
            freq[nums[i] + OFFSET] += 1

        def find_xth_smallest():
            count = 0
            for v in range(0, 50):
                count += freq[v]
                if count >= x:
                    return v - OFFSET
            return 0

        ans.append(find_xth_smallest())
        for i in range(k, len(nums)):
            freq[nums[i - k] + OFFSET] -= 1
            freq[nums[i] + OFFSET] += 1
            ans.append(find_xth_smallest())
        return ans