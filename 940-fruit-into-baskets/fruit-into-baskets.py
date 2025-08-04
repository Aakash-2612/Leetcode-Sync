class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        d = {}
        ans = float("-inf")
        for r in range(len(fruits)):
            d[fruits[r]] = 1 + d.get(fruits[r], 0)
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            ans = max(ans, sum(d.values()))
        
        return ans
        
