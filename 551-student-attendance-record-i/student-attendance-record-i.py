class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in s:
            if i == 'A':
                count += 1
        
        if count < 2 and 'LLL' not in s:
            return True
        else:
            return False