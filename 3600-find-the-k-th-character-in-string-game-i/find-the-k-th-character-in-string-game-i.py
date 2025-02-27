class Solution:
    def kthCharacter(self, k: int) -> str:
        def help(s):
            l = len(s)
            if l >= k:
                return s
            
            for i in range(l):
                s += chr(ord("a") + ((ord(s[i]) - ord("a"))+ 1)%26)
            return help(s)
        
        return help("a")[k-1]