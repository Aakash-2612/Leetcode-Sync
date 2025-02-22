class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []

        def backtracking(i):
            if len(cur) == k:
                ans.append(cur[:])
                return
            
            for num in range(i, n+1):
                cur.append(num)
                backtracking(num+1)
                cur.pop()
        
        backtracking(1)
        return ans