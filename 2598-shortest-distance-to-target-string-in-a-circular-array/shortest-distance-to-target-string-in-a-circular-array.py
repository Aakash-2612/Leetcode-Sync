class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        arr = words + words + words
        start = len(words) + startIndex + 1
        ans = float("inf")
        # print(start)
        for index, i in enumerate(arr):
            if i == target:
                # print(index, start)
                ans = min(ans, abs((index+1) - start))
        
        return ans if ans != float('inf') else -1