import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        for i in answers:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        ans = 0
        for key in d.keys():
            ans += (math.ceil(d[key]/(key+1)))*(key+1)
        
        return ans
