class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        row = len(grid[0])
        col = len(grid)
        arr = [0 for i in range(1, (row**2)+1)]
        ans = [-1, -1]
        s = 0

        for i in range(row):
            for j in range(col):
                if arr[(grid[i][j])-1] == 0:
                    arr[(grid[i][j])-1] = 1
                else:
                    ans[0] = grid[i][j]
                s += grid[i][j]
        
        n = row**2
        ans[1] = (n*(n+1)//2) - (s - ans[0])
        return ans
        