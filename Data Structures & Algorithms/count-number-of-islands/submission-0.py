from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 # no. of islands
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr >= ROWS or
                        nr < 0 or
                        nc >= COLS or
                        nc < 0 or
                        grid[nr][nc] == "0" or
                        (nr, nc) in visited
                    ):
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1

        return res