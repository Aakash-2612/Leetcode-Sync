class Solution:
    def scoreBalance(self, s: str) -> bool:
        tot = 0
        for i in s:
            tot += ord(i) - 96
        
        left = 0
        for i in range(len(s)):
            left += ord(s[i]) - 96
            right = tot - left
            if left == right:
                return True
        
        return False