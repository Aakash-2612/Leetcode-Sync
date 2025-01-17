class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)):
            d = {}
            temp = False
            for j in range(i, len(s)):
                d[s[j]] = 1 + d.get(s[j], 0)
                if d[s[j]] == k:
                    temp = True
                if temp:
                    count += 1
        
        return count