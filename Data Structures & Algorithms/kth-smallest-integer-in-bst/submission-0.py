# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Pattern: DFS Inorder Traversal on BST.

        Key idea:
        In a BST, inorder traversal visits nodes in sorted order:
        left subtree -> current node -> right subtree.

        So, if we count nodes as we visit them in inorder,
        the kth visited node is the kth smallest value.

        We use early stopping:
        Once i == k, we already found the answer, so we stop doing extra DFS work.

        Time: O(H + k) with early stopping, where H is the tree height.
              Worst case O(n), if k is large or the tree is skewed.
        Space: O(H) for the recursion stack.
               Worst case O(n) for a skewed tree.
        """
        res = root.val
        i = 0
        # inorder dfs. preserves sort in bst
        # proces order = leftmost -> current node -> rightmost
        def dfs(node):
            nonlocal i, res
            # base case
            if not node:
                return
            
            # process leftmost first
            dfs(node.left)

            # DONT process current node if i == k (if kth was found in leftmost earlier)
            if i == k:
                return
            i += 1
            if i == k:
                res = node.val
                return
            
            # process rightmost last
            dfs(node.right)

        dfs(root)
        return res
            