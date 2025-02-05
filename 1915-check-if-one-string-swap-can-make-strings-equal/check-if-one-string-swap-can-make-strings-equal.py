class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        arr = [i for i in s2]
        ind = 0
        res = []
        for i, j in zip(s1, s2):
            if i != j:
                res.append(ind)
            ind += 1
        
        if len(res) <= 1 or len(res) > 2:
            return False
        arr[res[0]], arr[res[1]] = arr[res[1]], arr[res[0]]
        if ''.join(arr) == s1:
            return True
        return False