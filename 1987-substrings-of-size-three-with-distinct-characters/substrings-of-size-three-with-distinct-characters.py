class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        l = 0
        d = {}
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                while s[r] in d:
                    del d[s[l]]
                    l += 1
                d[s[r]] = 1
            if len(d) == 3:
                ans += 1
                del d[s[l]]
                l += 1

        return ans