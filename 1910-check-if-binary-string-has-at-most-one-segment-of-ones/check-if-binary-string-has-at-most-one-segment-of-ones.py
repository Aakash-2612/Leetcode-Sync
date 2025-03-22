class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        d = Counter(s)
        ans = True
        flag = False
        size = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i] == '1':
                size += 1
                flag = True
            if flag and s[i] == '0':
                break
        
        if not flag:
            if d['1'] >= 2:
                return False
            else:
                return True
        else:
            print(size)
            if size != d['1']:
                return False
            return True