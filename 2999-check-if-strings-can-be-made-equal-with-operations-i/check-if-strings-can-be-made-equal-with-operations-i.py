class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            c1 = s1[2] + s1[1] + s1[0] + s1[3]
            c2 = s1[2] + s1[3] + s1[0] + s1[1]
            c3 = s1[0] + s1[3] + s1[2] + s1[1]

            if c1 == s2 or c2 == s2 or c3 == s2:
                return True
            else:
                return False