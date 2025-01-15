class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = Counter(word)
        s = set(word)
        for i in s:  
            char_num = len(s)
            d[i] -= 1
            if d[i] == 0:
                char_num -= 1
                del d[i]
            cur_sum = sum(d.values())
            if cur_sum%char_num == 0 and len(set(d.values())) == 1:
                return True
            d[i] = 1 + d.get(i, 0)
        
        return False
