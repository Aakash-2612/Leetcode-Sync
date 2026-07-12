class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        res = []
        d = {}
        count = 1
        for i in arr2:
            if i not in d:
                d[i] = count
                count += 1

        for i in arr:
            if i in d:
                res.append(d[i])
        
        return res