class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        arr = sorted(nums, reverse=True)
        min_ans = float("inf")
        for i in range(0, len(arr)-k+1):
            min_ans = min(min_ans, arr[i:i+k][0] - arr[i:i+k][k-1])
        return min_ans
