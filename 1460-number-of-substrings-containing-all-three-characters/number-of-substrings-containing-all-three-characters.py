class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        d = {'a': -1,
             'b': -1,
             'c': -1}
        for index, i in enumerate(s):
            d[i] = index
            if d['a'] >= 0 and d['b'] >= 0 and d['c'] >= 0:
                count += min(d['a'], d['b'], d['c']) + 1
        
        return count