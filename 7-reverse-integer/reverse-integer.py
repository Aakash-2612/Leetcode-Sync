class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x < 0:
            s = str(x)[1:]
            ans = -int(s[::-1])
        else:
            s = str(x)
            ans = int(s[::-1])

        if ans in range(-2**31, 2**31):
            return ans
        else:
            return 0