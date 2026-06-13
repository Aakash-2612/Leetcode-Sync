class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d = {}
        for i in range(len(weights)):
            d[i] = weights[i]
        ans = ''
        for i in words:
            temp = 0
            for j in i:
                temp += d[ord(j) - 97]
            ans += chr(122 - (temp%26))
        return ans