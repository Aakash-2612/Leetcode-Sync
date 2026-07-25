class Solution:
    def maxProduct(self, n: int) -> int:
        s = [int(i) for i in str(n)]
        arr = sorted(s, reverse=True)
        return arr[0] * arr[1]