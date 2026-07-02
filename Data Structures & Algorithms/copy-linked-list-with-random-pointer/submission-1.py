"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Two pass approach
        """
        cur = head
        old_list_copy = {}
        old_list_copy[None] = None

        # first pass: copy and create the nodes, but don't connect
        while cur:
            copy = Node(cur.val)
            old_list_copy[cur] = copy
            cur = cur.next

        cur = head

        # second pass: add connections
        while cur:
            copy = old_list_copy[cur]
            copy.next = old_list_copy[cur.next]
            copy.random = old_list_copy[cur.random]
            cur = cur.next
        return old_list_copy[head]
