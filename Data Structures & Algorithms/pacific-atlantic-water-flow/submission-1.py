class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Pattern: DFS from border

        Problem:
        Given a grid of heights, water can flow from a cell to another cell
        if the next cell has height less than or equal to the current cell.
        Return all cells where water can flow to both:
        - Pacific Ocean: top row and left column
        - Atlantic Ocean: bottom row and right column

        Key idea:
        Instead of starting DFS from every cell and checking whether it can
        reach both oceans, we reverse the direction.

        Start DFS from each ocean border and move inward only to cells that are
        greater than or equal to the previous height.

        Why this works:
        If we can move from the ocean border to a cell by only going uphill,
        then water from that cell can flow downhill back to that ocean.

        We store:
        - pacific: cells that can reach the Pacific
        - atlantic: cells that can reach the Atlantic

        The answer is the intersection of both sets.

        Time: O(ROWS * COLS), because each cell is visited at most once
        for each ocean.
        Space: O(ROWS * COLS), because the sets and recursion stack can store cells.
        """
        # check if each cell can go into atlantic and pacific ocean separately
        # Afterwards go through each set and return values that appear in both
        # this can be done through dfs. Each cell checks if it can reach the mentioned ocean,
        # if it cant, stop. If it can, add that cell to the set and then check its neighbors.
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        # it will update both the sets with the information
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(r, c, visit, prev_height):
            # base case: out of bound cell or height is less than prev_height (cannot goto ocean)
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
                # The current cell's height becomes the previous height
                # for the next recursive call.
                dfs(nr, nc, visit, heights[r][c])
            

        # Start dfs from top and bottom borders
        for c in range(COLS):
            # for the top row neighboring pacific
            dfs(0, c, pacific, heights[0][c])

            # for the bottom row neighboring atlantic
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # Start DFS from the left and right borders.
        for r in range(ROWS):
            # for the left col neighboring pacific
            dfs(r, 0, pacific, heights[r][0])

            # for the right row neighboring atlantic
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        # now each set contains cells that can reach that ocean
        # we need to return cells that are in both sets
        return list(atlantic.intersection(pacific))