from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = deque()
        visited = set()
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q:
            # len(q) is important as it creates a snapshot of
            # current items in the queue. This helps to calculate distance.
            for i in range(len(q)):
                # update grid with dist
                r, c = q.popleft()
                grid[r][c] = dist

                # add neighbouring cells to q
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] == -1
                    ):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
                
            dist += 1
            