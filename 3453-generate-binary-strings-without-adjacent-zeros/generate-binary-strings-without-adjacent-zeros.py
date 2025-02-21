class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        s = '01'

        def backtracking(i, cur):
            if i == n:
                ans.append(cur[:])
                return
            
            for c in s:
                if cur:
                    if cur[-1] == '0' and c == '0':
                        continue
                    else:
                        backtracking(i+1, cur + c)
                else:
                    backtracking(i+1, cur + c)
        backtracking(0, '')
        return ans