class Solution:
    def check(self, s):
        d = {')' : '('}
        stack = []
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return True
        return False

    def generateParenthesis(self, n: int) -> List[str]:
        s = '()'
        ans = []
        def backtracking(i, cur):
            if i == 2*n:
                # print(cur[:])
                if self.check(cur):
                    ans.append(cur[:])
                return
            
            for c in s:
                backtracking(i+1, cur+c)
        
        backtracking(0, '')
        return ans