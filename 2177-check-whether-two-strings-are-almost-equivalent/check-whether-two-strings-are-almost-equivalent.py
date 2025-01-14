class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1 = Counter(word1)
        d2 = Counter(word2)
        ans = True
        s = set()
        for i in d1:
            if abs(d1[i] - d2.get(i, 0)) > 3:
                ans = False
            s.add(i)

        for i in d2:
            if abs(d2[i] - d1.get(i, 0)) > 3 and i not in s:
                ans = False
        return ans