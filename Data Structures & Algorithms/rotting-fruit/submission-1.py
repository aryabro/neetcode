from collections import deque
class Solution:
    """
        Pattern: Multi-Source BFS.

        Problem:
        Given a grid where:
        - 0 represents an empty cell
        - 1 represents a fresh orange
        - 2 represents a rotten orange
        Every minute, a rotten orange rots its fresh neighboring oranges
        in 4 directions: up, right, down, and left.
        Return the minimum number of minutes needed to rot all oranges.
        If some fresh oranges can never be reached, return -1.

        Key idea:
        This is a shortest-time spread problem, so BFS is a good fit.

        Instead of starting BFS from one rotten orange, we start from all
        initially rotten oranges at the same time. This is called multi-source BFS.

        Each BFS level represents one minute.
        - All oranges currently in the queue rot their neighbors.
        - After processing one full level, one minute has passed.

        Time: O(ROWS * COLS), because each cell is processed at most once.
        Space: O(ROWS * COLS), because the queue can store many cells.
        """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        # First pass:
        # 1. Count all fresh oranges.
        # 2. Add all initially rotten oranges to the queue.
        # We add all rotten oranges first because they all start spreading
        # at the same time at minute 0.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # store possible directions of each cell
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q and fresh > 0:

            # len(q) is the number of rotten oranges active this minute.
            # Any newly rotten oranges added during this loop will spread
            # in the next minute.
            for i in range(len(q)):
                r, c = q.popleft()
                
                # checking each neighbor
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    
                    # skip invalid cells or already rotten oranges
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != 1
                    ):
                        continue
                    
                    grid[nr][nc] = 2 # convert fresh orange to rotten to prevent double counting
                    q.append((nr, nc)) # add it to q so it can spread rot next min
                    fresh -= 1 # update fresh oranges count
            
            # increment time after one BFS level is complete
            time += 1
        
        return time if fresh == 0 else -1