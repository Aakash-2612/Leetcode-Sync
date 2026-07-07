class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        ans = ''
        count = 0
        for i in s:
            if i != '0':
                count += int(i)
                ans += i

        if len(ans) >= 1:
            return count * int(ans)
        else:
            return 0
        