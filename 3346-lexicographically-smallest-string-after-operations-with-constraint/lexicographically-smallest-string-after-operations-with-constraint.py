class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = ''
        for i in s:
            a = ord(i) - ord('a')
            b = (ord('z') - ord(i)) + 1
            # print(f'a = {a}, b = {b}, k = {k}')
            if k >= min(a, b):
                res += 'a'
                k -= min(a, b)
            else:
                res += chr(ord(i) - k)
                k = 0
        
        return res