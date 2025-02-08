class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if len(stack) != 0 and stack[-1] == d[i]:
                    stack.pop()
                else:
                    stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False