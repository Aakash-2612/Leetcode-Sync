class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        q = deque()
        visited = set()
        n, m = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    q.append((i, j))
                    directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

                    while q:
                        r, c = q.popleft()
                        for dr, dc, move in directions:
                            new_r, new_c = r + dr, c + dc

                            new_state = (new_r, new_c)
                            if 0 <= new_r < n and 0 <= new_c < m and new_state not in visited and grid[new_r][new_c] == "1":
                                visited.add(new_state)
                                q.append(new_state)

        return count
                                

