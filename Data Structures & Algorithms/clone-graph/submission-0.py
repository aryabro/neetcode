"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # tracks if we have already cloned the current node
        # does not track their neighbors(edges), recursion handles that automatically
        old_to_new = {}
        
        # returns copy of node
        def dfs_clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            # now clone is ready with val but no neighbors added
            clone = Node(node.val)
            old_to_new[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs_clone(nei))
            
            return clone
        
        return dfs_clone(node)
        


