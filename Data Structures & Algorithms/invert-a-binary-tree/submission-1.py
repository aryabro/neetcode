# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Pattern: DFS Tree Traversal.
        Possible approaches:
        1. Recursive DFS:
           At each node, swap the left and right children.
           Then recursively invert the left and right subtrees.
        2. Iterative BFS:
           Use a queue to visit nodes level by level.
           Swap each node's children as we visit it.
        3. Iterative DFS:
           Use a stack instead of recursion.

        This solution uses recursive DFS.

        Time: O(n), because we visit every node once.
        Space: O(h), where h is the height of the tree due to recursion stack.
               In a balanced tree, h = log n.
               In a skewed tree, h = n.
        """
        # base case
        if not root:
            return None

        # swap left and right children of current node
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root