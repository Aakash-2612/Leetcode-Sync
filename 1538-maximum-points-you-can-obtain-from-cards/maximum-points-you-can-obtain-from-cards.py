class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        temp = sum(cardPoints[:k])
        ans = temp
        j = len(cardPoints)-1
        for i in range(k-1, -1, -1):
            temp = (temp - cardPoints[i]) + cardPoints[j]
            ans = max(temp, ans)
            j -= 1
        
        return ans
        