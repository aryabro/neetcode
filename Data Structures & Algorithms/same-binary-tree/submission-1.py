# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Pattern: Binary Tree DFS / Recursion.

        Possible approaches:
        1. DFS recursion:
           Compare the two trees node by node.
           At each step, compare p and q, then recursively compare
           their left children and right children.

        2. BFS iteration:
           Use a queue to compare nodes level by level.

        Time: O(n), where n is the number of nodes in the smaller/common traversal.
              In the worst case, we visit every node in both trees.
        Space: O(h), where h is the height of the tree due to recursion stack.
               Worst case O(n) for a skewed tree, O(log n) for a balanced tree.
        """
        # returns bool while comparing equivalence of two trees
        def dfs(p, q):
            if not p and not q:
                return True
            
            # If only one exists or values differ, they do not match.
            if not p or not q or p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)