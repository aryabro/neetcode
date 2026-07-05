from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set() # (0,1), (0, 2)

        def bfs(r, c) -> int: # 0,1
            visited.add((r,c))
            area = 0
            q = deque() # 0,2
            q.append((r, c)) 
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while q:
                r, c = q.popleft() # 0, 1
                for dr, dc in directions:
                    nr = r + dr # 0
                    nc = c + dc # 2
                    
                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] == 0 or
                        (nr, nc) in visited
                    ):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))

                # we found valid cell of same island
                area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited: # 0,1
                    area = bfs(r, c)
                    res = max(res, area)
        
        return res


                    
