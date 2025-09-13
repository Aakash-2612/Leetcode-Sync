class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        cons, vow = 0, 0
        d_cons = defaultdict(int)
        d_vow = defaultdict(int)

        for i in s:
            if i not in vowels:
                d_cons[i] += 1
                if cons < d_cons[i]:
                    cons = d_cons[i]
            else:
                d_vow[i] += 1
                if vow < d_vow[i]:
                    vow = d_vow[i]
        
        return cons + vow