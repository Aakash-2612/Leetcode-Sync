class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        temp = False
        count = 0
        s = set()
        dig = ''
        for i in word:
            if i.isdigit():
                if not temp:
                    temp = True
                    dig += i
                else:
                    dig += i
            else:
                if temp:
                    if len(dig) >= 1 and int(dig) not in s:
                        count += 1
                        temp = False
                        s.add(int(dig))
                    dig = ''
        
        if temp and len(dig) > 0 and int(dig) not in s:
            count += 1
        return count
