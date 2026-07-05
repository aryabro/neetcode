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
        """
        Pattern: Graph DFS + Hash Map.

        Problem:
        Given a reference to a node in an undirected connected graph,
        return a deep copy of the graph.

        Key idea:
        Each original node needs exactly one cloned node.
        We use dfs to visit each neighbor of the provided node and create a copy.
        To avoid cycles, we keep track of each visited node
        We use a hash map:
            old_to_new[original_node] = cloned_node

        Time: O(V + E), because we visit every node and edge once.
        Space: O(V), because the hash map and recursion stack store nodes.
        """
        if not node:
            return None

        # tracks if we have already cloned the current node
        # does not track their neighbors(edges), recursion handles that automatically
        old_to_new = {}
        
        # returns clone of input node
        def dfs_clone(node):
            # if clone is created, reuse it
            if node in old_to_new:
                return old_to_new[node]
            
            # create clone of node. clone.neighbors is empty atp
            clone = Node(node.val)

            # store clone before going to neighbors to prevent infinity
            old_to_new[node] = clone

            # dfs is recursively called here. for each neighbor, create its copy
            for nei in node.neighbors:
                clone.neighbors.append(dfs_clone(nei))
            
            return clone # the fully connected cloned node is returned
        
        return dfs_clone(node)
        