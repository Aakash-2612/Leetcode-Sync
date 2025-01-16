class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        val = 0
        for r in range(len(s)):
            val += ord(s[r]) - ord('a')
            if (r+1) % k == 0:
                res.append(chr((val % 26) + ord('a'))) 
                val = 0
    
        return ''.join(i for i in res)