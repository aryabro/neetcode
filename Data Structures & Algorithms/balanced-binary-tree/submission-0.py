# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Pattern: DFS / Postorder Traversal.

        A binary tree is balanced if:
        1. The left and right subtree is balanced.
        2. The height difference between left and right subtree is at most 1.

        We use postorder DFS because each node needs information from its children
        before deciding whether the current subtree is balanced.

        For each node, dfs returns:
        [isBalanced, height]

        Time: O(n), because we visit each node once.
        Space: O(h), where h is the height of the recursion stack.
               Worst case: O(n) for a skewed tree.
               Best case: O(log n) for a balanced tree.
        """

        # returns [isBalanced, height]
        def dfs(node):
            
            # base case
            if not node:
                return [True,0]
            
            left, right = dfs(node.left), dfs(node.right)
            
            isBalanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            height = 1 + max(left[1], right[1])
            
            return [isBalanced, height]

        return dfs(root)[0]