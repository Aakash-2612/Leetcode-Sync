class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        for l in range(len(s)):
            d = {}
            for r in range(l, len(s)):
                d[s[r]] = 1 + d.get(s[r], 0)
                if d[s[r]] == k:
                    count += len(s) - r
                    break
        
        return count