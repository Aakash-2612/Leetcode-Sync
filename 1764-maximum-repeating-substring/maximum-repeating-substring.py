import math
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        for i in range(len(sequence)):
            ind = 0
            count = 0
            for j in range(i, len(sequence)):
                if ind == len(word):
                    count += 1
                    ind = 0
                if sequence[j] == word[ind]:
                    ind += 1
                else:
                    break
            if ind == len(word):
                count += 1
            ans = max(ans, count)
        
        return ans