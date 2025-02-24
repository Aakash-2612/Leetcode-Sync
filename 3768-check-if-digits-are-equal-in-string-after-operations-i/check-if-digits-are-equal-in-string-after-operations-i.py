class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        def helper(s):
            if len(s) <= 2:
                if len(set(s)) == 1:
                    return True
                return False

            new = ''
            for i in range(1, len(s)):
                new += str((int(s[i-1]) + int(s[i]))%10)
            return helper(new)
        return helper(s)