import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        ans = 0
        count = 0
        for i in word:
            if i not in d:
                count += 1
                if math.ceil(count/8) <= 1:
                    d[i] = 1
                elif math.ceil(count/8) <= 2:
                    d[i] = 2
                elif math.ceil(count/8) <= 3:
                    d[i] = 3
                else:
                    d[i] = 4
            ans += d[i]

        # print(d)
        return ans
                    