class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            l = len(i)
            for j in range(len(word)):
                if word[j:j+l] == i:
                    count += 1
                    break
        
        return count