# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
    
        # returns the maximum sum WITHOUT split
        # updates res if splitting is allowed (checks if max_sum_path goes through itself)
        # postorder dfs
        def dfs(root):
            # base case
            if not root:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)

            # deal with negative sums (if total is -ve, we dont consider it)
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)
            
            # update res if split allowed
            res[0] = max(res[0], root.val + max_left + max_right)

            max_without_splitting = root.val + max(max_left, max_right)
            return max_without_splitting

        dfs(root)

        return res[0]
