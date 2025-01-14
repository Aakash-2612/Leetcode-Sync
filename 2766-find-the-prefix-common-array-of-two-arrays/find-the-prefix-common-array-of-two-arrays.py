class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        s = set()
        ans = []
        for i, j in zip(A, B):
            if i == j:
                count += 1
            else:
                if i in s:
                    count += 1
                if j in s:
                    count += 1
            s.add(i)
            s.add(j)
            ans.append(count)
            
        return ans