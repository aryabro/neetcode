from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Pattern: Multi-Source BFS.

        Problem:
        Given a grid where:
        - -1 represents water/wall
        - 0 represents treasure
        - INF represents land/empty room
        Fill each land cell with the shortest distance to the nearest treasure.
        The grid is modified in-place.

        Key idea:
        Instead of running BFS separately from every land cell, start BFS from
        all treasures at the same time.

        Since all treasures begin at distance 0, the first time BFS reaches
        a land cell, that distance is guaranteed to be the shortest distance
        from the nearest treasure.

        Each BFS level represents one distance step away from any treasure.

        Time: O(ROWS * COLS), because each cell is visited at most once.
        Space: O(ROWS * COLS), because the queue and visited set can store cells.
        """
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # for neighbors
        q = deque() # for bfs
        # for tracking visited nodes. First time they are 
        # visited, its guaranteed to be the shortest distance.        
        visited = set()
        dist = 0

        # First pass:
        # Add all treasures to the queue as BFS starting points.
        # This is what makes the BFS "multi-source".
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q:
            # len(q) gives a snapshot of the current BFS layer.
            # Every cell currently in the queue has the same distance
            # from the nearest treasure.
            for i in range(len(q)):
                # process current cell
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
            
            # for multi-source bfs, every cell at current distance
            # has been processed now by the for loop.
            dist += 1
            