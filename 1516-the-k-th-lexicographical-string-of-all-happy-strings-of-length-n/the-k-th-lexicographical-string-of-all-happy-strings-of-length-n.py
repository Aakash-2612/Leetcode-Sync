class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        s = 'abc'

        def backtracking(i, cur):
            if i == n:
                ans.append(cur)
                return 
            
            for c in s:
                if len(cur) > 0 and cur[-1] == c:
                    continue
                backtracking(i+1, cur+c)
        
        backtracking(0, '')
        return ans[k-1] if k <= len(ans) else ""