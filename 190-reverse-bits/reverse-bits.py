class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        rem = 32 - len(b)
        rev = b[::-1] + ('0'*rem)
        return int(rev, 2)