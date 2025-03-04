class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtracking(i, cur):
            if cur == n:
                return True
            if cur > n or 3 ** i > n:
                return False
            
            if backtracking(i+1, cur + 3**i):
                return True
            return backtracking(i+1, cur)
        
        return backtracking(0, 0)