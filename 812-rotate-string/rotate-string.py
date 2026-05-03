class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s
        l = len(goal)

        for i in range(len(s)):
            if s[i:i+l] == goal:
                return True
        
        return False