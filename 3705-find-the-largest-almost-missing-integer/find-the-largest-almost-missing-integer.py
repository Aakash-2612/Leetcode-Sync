class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {}

        for i, num in enumerate(nums):
            left = max(0, i - k + 1)
            right = min(i, n - k)

            if num not in d:
                d[num] = []
            d[num].append((left, right))
        ans = -1

        for num, intervals in d.items():
            intervals.sort()
            total = 0
            start, end = intervals[0]

            for l, r in intervals[1:]:
                if l <= end + 1:
                    end = max(end, r)
                else:
                    total += end - start + 1
                    start, end = l, r

            total += end - start + 1

            if total == 1:
                ans = max(ans, num)

        return ans