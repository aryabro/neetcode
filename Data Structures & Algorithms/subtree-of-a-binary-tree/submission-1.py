# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Pattern: Tree DFS + Same Tree Check.

        isSubtree searches for where subRoot could start.
        is_same_tree checks whether two trees are exactly identical from that starting point.
        
        def isSubtree:
            We visit each node in the main tree and ask:
                "Does the subtree starting starting from you exactly match subRoot?"
            
            He checks it with the is_same_tree function.
            If it return True, we got our answer and return it.
            If it returns False, this current node is not the starting point.
            So we recursively ask the left child and right child the same question.

        def is_same_tree:
            We compare two trees starting from their current nodes.
            First, check whether the current nodes match.
            If they match, recursively compare their left children and right children.
        
        Time: O(n * m), where n is the number of nodes in root and m is the
        number of nodes in subRoot. In the worst case, we may compare subRoot
        against many nodes in root.
        Space: O(h), where h is the recursion depth of the tree.
        Worst case O(n) for a skewed tree.
        """
        # Empty subRoot is always considered a subtree.
        if not subRoot: return True

        # If root is empty but subRoot is not empty, then subRoot
        # cannot exist inside root.
        if not root: return False

        # if both are same, convey the same to parents
        if self.is_same_tree(root, subRoot):
            return True
        
        # If the current node is not the starting point of subRoot,
        # search the left and right subtrees.
        # If either side contains subRoot, return True, and answer is bubbled to start
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    
    def is_same_tree(self, p, q):

        # if both don't exist, then they are equal
        if not p and not q:
            return True

        # if current node is equal, recursively compare both children as well
        if p and q and p.val == q.val:
            return (self.is_same_tree(p.left, q.left) and 
                    self.is_same_tree(p.right, q.right)
                    )

        return False
