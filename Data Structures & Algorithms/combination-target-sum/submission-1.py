class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Pattern: Backtracking / DFS.

        Problem:
        Given a list of distinct positive integers and a target, return all unique
        combinations where the chosen numbers sum to target.

        Important detail:
        Each number can be used unlimited times.

        Key idea:
        At each index i, we have 2 choices:
        1. Include nums[i]
           - Stay at the same index i because nums[i] can be reused.
        2. Exclude nums[i]
           - Move to i + 1 because we are done considering nums[i].

        Example:
        nums = [2, 3, 6, 7], target = 7

        One valid path:
        choose 2 -> choose 2 -> choose 3
        total = 7
        combination = [2, 2, 3]

        Time: O(2**(target/min(nums))) approximately.
              The recursion tree depends on how many times values can be reused.
              Simplify to O(2**t)

        Space: O(target/min(nums)) for the recursion depth, excluding the output.
        """
        res = []

        def dfs_backtrack(i:int, cur:list, total:int ):
            # stop and return if total is target
            if total == target:
                res.append(cur.copy())
                return

            # return if i>len or total exceeds target, to avoid processing irrelevant results
            if i >= len(nums) or total > target:
                return
            
            # stay at i because same number can be reused
            # hence total is also updated
            cur.append(nums[i])
            new_total = total + nums[i]
            dfs_backtrack(i, cur, new_total)

            # Move to the next index because we are done using nums[i].
            cur.pop() # remove i from list
            dfs_backtrack(i + 1, cur, total)

        dfs_backtrack(0, [], 0)
        return res