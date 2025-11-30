class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        res = len(nums)
        cur_sum = 0
        # map rem of prefix sums to last index
        d = {
            0: -1  # starting element is divisble by p
        }
        for index, i in enumerate(nums):
            cur_sum = (cur_sum + i) % p
            prefix = (cur_sum - rem + p) % p
            if prefix in d:
                length = index - d[prefix]
                res = min(res, length)
            d[cur_sum] = index

        return -1 if res == len(nums) else res