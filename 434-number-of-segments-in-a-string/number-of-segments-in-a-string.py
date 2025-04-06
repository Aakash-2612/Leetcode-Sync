class Solution:
    def countSegments(self, s: str) -> int:
        arr = s.split(' ')
        count = 0
        for i in arr:
            for j in i:
                if j != ' ':
                    count += 1
                    break
        
        return count