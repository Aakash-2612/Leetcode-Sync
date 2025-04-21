class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        to_chars = set()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in to_chars:
                    return False
                d[s[i]] = t[i]
                to_chars.add(t[i])
        return True