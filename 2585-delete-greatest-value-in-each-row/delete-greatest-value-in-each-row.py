class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for i in range(col-1, -1, -1):
            temp = []
            for j in range(row):
                temp.append(grid[j][i])
            ans += max(temp)
            
        return ans