class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        l = 0
        ans = len(s)
        d = {'W': 0,
             'B': 0}
        for r in range(len(s)):
            d[s[r]] += 1
            if (r - l + 1)%k == 0:
                ans = min(ans, d['W'])
                d[s[l]] -= 1
                l += 1
        
        return ans