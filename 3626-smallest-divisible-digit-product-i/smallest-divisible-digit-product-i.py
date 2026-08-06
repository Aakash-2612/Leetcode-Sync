def fun(n):
    s = str(n)
    res = 1
    for i in s:
        res *= int(i)
    
    return res

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p = fun(n)
            if p == 0 or p%t == 0:
                return n
            else:
                n += 1
        