from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Pattern: Graph Traversal on a Grid using BFS.

        Problem:
        Given a 2D grid of "1"s and "0"s:
        - "1" represents land
        - "0" represents water
        Return the number of islands.

        Key idea:
        Treat each land cell as a graph node.
        From each land cell, we can move in 4 directions:
        up, right, down, and left.

        When we find an unvisited land cell, that means we found a new island.
        Then we run BFS from that cell to visit every connected land cell
        in that same island.

        Time: O(ROWS * COLS), because each cell is visited at most once.
        Space: O(ROWS * COLS), because visited and queue can store cells.
        """
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 # no. of islands
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c)) # add starting land cell to queue
            visited.add((r, c)) # mark visited immediately

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            while q:
                row, col = q.popleft()

                # check all neighbouring cells
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # 1-4: out of bounds, 5: water, 6: visited
                    if (nr >= ROWS or
                        nr < 0 or
                        nc >= COLS or
                        nc < 0 or
                        grid[nr][nc] == "0" or
                        (nr, nc) in visited
                    ):
                        continue

                    # valid cell added to queue and visited set
                    q.append((nr, nc))
                    visited.add((nr, nc))

        # scan every cell on grid
        for r in range(ROWS):
            for c in range(COLS):
                
                # if True, we found unvisited land i.e. new island, 
                # completely map it with BFS
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1 # one bfs call fully explores island

        return res