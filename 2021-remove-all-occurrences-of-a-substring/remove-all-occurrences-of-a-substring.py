class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        l = len(part)
        for i in s:
            try:
                while "".join(stack[len(stack)-l:]) == part:
                    for j in range(l):
                        stack.pop()
            except:
                pass
            stack.append(i)
        
        if "".join(stack[len(stack)-l:]) == part:
            for i in range(l):
                stack.pop()
        
        return "".join(stack)