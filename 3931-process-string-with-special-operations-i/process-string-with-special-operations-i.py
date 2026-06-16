class Solution:
    def processStr(self, s: str) -> str:
        ans = ''
        for i in s:
            if i == '*':
                if len(ans) >= 1:
                    temp = ans[:-1]
                    ans = temp
            elif i == '#':
                ans += ans
            elif i == '%':
                ans = ans[::-1]
            else:
                ans += i
        
        return ans