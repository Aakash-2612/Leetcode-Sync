class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def helper(s):
            val = 0
            for i in s:
                val += int(i) 
            return val
        ans = 0
        for i in range(low, high+1):
            i = str(i)
            if len(i) % 2 != 0:
                continue
            s1 = i[:len(i)//2]
            s2 = i[len(i)//2:]
            if helper(s1) == helper(s2):
                ans += 1
        
        return ans
