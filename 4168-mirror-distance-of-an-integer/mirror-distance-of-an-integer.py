class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = int(str(n)[::-1])
        print(rev)
        return abs(n - rev)