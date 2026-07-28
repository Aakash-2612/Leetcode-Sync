class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        ans = ''
        res = ''
        mid = None
        for i in range(97, 123):
            c = chr(i)
            if c in d:
                if d[c] % 2 != 0:
                    mid = c
                ans += c * (d[c]//2)
        
        # print(mid)
        if mid:
            res = ans + mid + ans[::-1]
        else:
            res = ans + ans[::-1]
        return res