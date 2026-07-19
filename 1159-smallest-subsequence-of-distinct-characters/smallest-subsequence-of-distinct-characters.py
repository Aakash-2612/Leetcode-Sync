class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = [False for i in range(26)]
        lastInd = [-1 for i in range(26)]
        for index, i in enumerate(s):
            lastInd[ord(i) - ord('a')] = index

        stack = []
        for index, i in enumerate(s):
            if not stack:
                stack.append(i)
                seen[ord(i) - ord('a')] = True
            else:
                if not seen[ord(i) - ord('a')]:
                    while stack and ord(stack[-1]) > ord(i) and lastInd[ord(stack[-1]) - ord('a')] > index:
                        seen[ord(stack[-1]) - ord('a')] = False
                        stack.pop()
                    stack.append(i)
                    seen[ord(i) - ord('a')] = True
                
        return "".join(stack)