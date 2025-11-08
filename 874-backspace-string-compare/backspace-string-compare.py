class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s1=list(s)
        # s2=list(t)
        # print(s1)
        # for i in range(len(s1)):
        #     if s1[i]=='#':
        #         s1.remove(s1[i-1])
        # for i in range(len(s2)):
        #     if s2[i]=='#':
        #         s2.remove(s2[i-1])
        # ar1=" ".join(s1)
        # ar2=" ".join(s2)
        # if ar1==ar2:
        #     return True
        # else:
        #     return False
        
        stack = []
        for i in s:
            if i == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        
        new_s = ''.join(map(str, stack))
        
        stack = []
        for i in t:
            if i == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        
        new_t = ''.join(map(str, stack))
               
        return new_s == new_t