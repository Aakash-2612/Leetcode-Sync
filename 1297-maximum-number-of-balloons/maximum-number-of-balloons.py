class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }

        for i in text.lower():
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        # print(d)
        cntB = d['b']
        cntA = d['a']
        cntN = d['n']
        cntL = d['l'] // 2
        cntO = d['o'] // 2

        return min(cntB, cntA, cntL, cntO, cntN)