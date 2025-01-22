class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in d:
                stack.append(s[i])
            else:
                if len(stack) > 0 and d.get(stack[-1], None):
                    if d[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        if len(stack) == 0:
            return True
        return False