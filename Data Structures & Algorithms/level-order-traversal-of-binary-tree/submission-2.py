# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Pattern: BFS

        BFS is a good fit because a queue lets us process nodes in the same
        order they appear from top to bottom, left to right.

        - Use a queue to store nodes we still need to visit.
        - For each level, first save the current queue length.
        - That length tells us exactly how many nodes belong to this level.
        - Process only those nodes, while adding their children for the next level.

        Time: O(n), because each node is visited once.
        Space: O(n), because the queue can store up to one level of nodes.
        """
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            # These nodes belong to the current level.
            len_queue = len(queue)

            # Stores nodes for current level
            level = []

            for _ in range(len_queue):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            
            # Only add non-empty levels
            if level:
                res.append(level)
        return res
