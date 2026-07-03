# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Pattern: Binary Tree DFS / Postorder Traversal.

        Problem:
        Find the maximum path sum in a binary tree.

        Key idea:
        At each node, we calculate two things:
        1. Maximum path sum WITH splitting:
           left path + current node + right path

           This is a complete path using the current node as the turning point.
           We use this to update the global answer.

        2. Maximum path sum WITHOUT splitting:
           current node + max(left path, right path)

           This is what we return to the parent, because a parent can only extend
           one single path from this node. We cannot return both left and right,
           because that would create a split.

        Time: O(n), because we visit every node once.
        Space: O(h), where h is the height of the tree due to recursion stack.
        Worst case space is O(n) for a skewed tree.
        """
        res = root.val
    
        # returns the maximum sum WITHOUT split
        # updates res if splitting is allowed (checks if max_sum_path goes through itself)
        # postorder
        def dfs(root):
            nonlocal res
            # base case
            if not root:
                return 0

            # postorder : get best path sums from children first
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            # ignore if child path is -ve
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)
            
            # best path with split
            max_with_split = root.val + max_left + max_right
            res = max(res, max_with_split)

            # We return best path without split
            max_without_splitting = root.val + max(max_left, max_right)
            return max_without_splitting

        dfs(root)

        return res
