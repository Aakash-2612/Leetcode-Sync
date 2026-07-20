class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        arr = [num for row in grid for num in row]
        
        k %= len(arr)
        arr = arr[-k:] + arr[:-k]

        return [arr[i:i + cols] for i in range(0, len(arr), cols)]