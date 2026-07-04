class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Pattern: Backtracking.

        Problem:
        Given a list of distinct numbers, return all possible permutations.

        Key idea:
        Build one permutation step by step using a temporary list `sol`.

        At each recursive level:
        - Try every num in nums.
        - If the num is not already in the current permutation, choose it.
        - Recursion to fill the next position.
        - Undo the choice using pop() so we can try another number for next loop.
        - Undo and redo is done because we are just reusing the res array/list.

        Example:
        nums = [1, 2, 3]

        One path:
        sol = [1]
        sol = [1, 2]
        sol = [1, 2, 3] -> add copy to ans
        backtrack, remove 3
        backtrack, remove 2
        try 3 next...

        Time: O(n! * n)
              There are n! permutations, and copying each permutation takes O(n).
              Also, `x not in sol` costs O(n), so this implementation has extra overhead.

        Space: O(n)
               Recursion depth and current path `sol` use O(n).
               Output space is O(n! * n), because we store all permutations.
        """
        res = [] # stores final Output
        sol = [] # stores list for each recursion which is appended to res

        def dfs_backtrack():
            # base case: if solution len is equal to input array, we have reached end
            # append to res
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            
            # Try placing each number at the current position.
            for num in nums:

                # Only use a number if it is not already in the current permutation.
                # This prevents duplicates inside one permutation.
                if num not in sol:
                    sol.append(num)
                    dfs_backtrack()
                    sol.pop()

        dfs_backtrack()
        return res
