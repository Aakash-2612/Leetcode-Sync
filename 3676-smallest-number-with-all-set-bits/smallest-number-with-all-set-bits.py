class Solution:
    def smallestNumber(self, n: int) -> int:
        val = bin(n)[2:]
        l = len(val)
        ans = '1'*l
        return int(ans, 2)