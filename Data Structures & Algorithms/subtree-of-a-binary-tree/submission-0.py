# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        My thought process to understand this question.
        Imagine if we take a little kid to a old great grandfather and ask him
        "Is he a clone of your descendant?"

        The great grandfather is like I don't know, let me ask my children
        The children will only know if statement is true if the clone is directly
        their child, they don't care about others, so they ask their children.
        This continues till we reach the original parent, who is like "Yeah thats the 
        clone of my kid". Then the parent tells that to his parent and so on till 
        we reach the great grandfather again, who gives us the answer.
        """
        # if root exists, but subRoot doesn't, then subRoot is present in root
        if not subRoot: return True

        # if subRoot exists, but root doesn't, then condition is invalid (None can't have children)
        if not root: return False

        # if both are same, convey the same to parents
        if self.is_same_tree(root, subRoot):
            return True
        
        # if root != subRoot, ask the same to both children of root
        # the great grandfather asks their children, and answer is bubbled to him
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    
    def is_same_tree(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return (self.is_same_tree(p.left, q.left) and 
                    self.is_same_tree(p.right, q.right)
                    )

        return False




