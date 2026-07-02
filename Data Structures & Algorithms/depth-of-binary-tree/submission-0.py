# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_child_depth = self.maxDepth(root.left)
        right_child_depth = self.maxDepth(root.right)

        return 1 + max(left_child_depth, right_child_depth)
        