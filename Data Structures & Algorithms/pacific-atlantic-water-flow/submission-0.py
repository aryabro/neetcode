class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # check if each cell can go into atlantic and pacific ocean separately
        # Afterwards go through each set and return values that appear in both
        # this can be done through dfs. Each cell checks if it can reach the mentioned ocean,
        # if it cant, stop. If it can, add that cell to the set and then check its neighbors.
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        # it will update both the sets with the information
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(r, c, visit, prev_height):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visit or
                heights[r][c] < prev_height
            ):
                return
            
            visit.add((r, c))
            
            # check neighbors recursively
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # new row, new col, same ocean, original cell height
                dfs(nr, nc, visit, heights[r][c])
            

        # we will start from each line neighboring to the ocean
        for c in range(COLS):
            # for the top row neighboring pacific
            dfs(0, c, pacific, heights[0][c])

            # for the bottom row neighboring atlantic
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            # for the left col neighboring pacific
            dfs(r, 0, pacific, heights[r][0])

            # for the right row neighboring atlantic
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        # now each set contains cells that can reach that ocean
        # we need to return cells that are in both sets

        return list(atlantic.intersection(pacific))