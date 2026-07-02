# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        # returns height
        def dfs(curr):
            if not curr:
                return 0
            
            left_sub_height = dfs(curr.left)
            right_sub_height = dfs(curr.right)

            nonlocal diameter

            diameter = max(diameter, left_sub_height + right_sub_height)
            height = 1 + max(left_sub_height, right_sub_height)
            return height

        dfs(root)
        return diameter