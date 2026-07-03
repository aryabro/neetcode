# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        # preorder traversal
        def dfs(node):
            # base case
            if not node:
                res.append("N")
                return None
            
            # if node exists, append val as str to list
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        # return list(res) as str()
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i = 0

        # returns Node or None
        def dfs():
            nonlocal i
            # base case
            if vals[i] == "N":
                i += 1
                return
            
            node = TreeNode(int(vals[i]))

            # increment i before calling dfs()
            i += 1

            # add node attributes, .val adding during creation
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

            







