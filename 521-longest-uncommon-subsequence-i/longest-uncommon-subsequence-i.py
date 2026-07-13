class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return len(max(a, b, key=lambda x: len(x)))