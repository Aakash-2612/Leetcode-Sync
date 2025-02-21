class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtracking(i, cur):
            if i == len(s):
                ans.append(cur[:])
                return
            
            if s[i].isalpha():
                cur = cur[:i] + s[i].upper() + cur[i+1:]
                backtracking(i+1, cur)
                cur = cur[:i] + s[i].lower() + cur[i+1:]
                backtracking(i+1, cur)
            else:
                backtracking(i+1, cur)
        backtracking(0, s)
        return ans