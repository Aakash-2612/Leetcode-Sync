class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            d1 = str(i)
            if '0' not in d1:
                d2 = str(n-i)
                if '0' not in d2:
                    return [i, n-i]
