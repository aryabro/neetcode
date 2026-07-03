# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Pattern: Tree DFS / Postorder Traversal.

        Find Diameter i.e. Longest path between any two nodes of tree.
        Diameter is measured in edges.

        Main idea:
        For every node, calculate the height of its left and right subtrees.
        The longest path passing through that node is:

            left subtree height + right subtree height

        We keep a running maximum diameter while DFS returns subtree heights.

        Time: O(n), because every node is visited once.
        Space: O(h), where h is the height of the tree due to recursion stack.
               Worst case O(n) for a skewed tree.
               Best/average O(log n) for a balanced tree.
        """
        # diameter at each node is sum of height of two children
        diameter = 0

        # returns height
        def dfs(curr):
            """
            Returns the height of the subtree rooted at curr.
            - Empty node has height 0.
            - Leaf node has height 1.

            While returning height upward, we also update diameter.
            """
            nonlocal diameter

            # base case
            if not curr:
                return 0
            
            # Postorder dfs -> get left, right child height first
            left_sub_height = dfs(curr.left)
            right_sub_height = dfs(curr.right)

            # Update nonlocal "diameter" if its max seen so far
            diameter = max(diameter, left_sub_height + right_sub_height)

            height = 1 + max(left_sub_height, right_sub_height)
            return height

        dfs(root)
        return diameter