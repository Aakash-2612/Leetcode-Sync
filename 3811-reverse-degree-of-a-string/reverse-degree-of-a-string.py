class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for index, i in enumerate(s):
            ans += (26 - (ord(i) - ord('a'))) * (index + 1)
        return ans