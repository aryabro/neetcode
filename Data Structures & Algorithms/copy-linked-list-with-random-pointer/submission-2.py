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
        Pattern: Two pass with Hash Map

        Question: We need to create a deep copy of a linked list where each node has:
        - next pointer: points to the next node
        - random pointer: can point to any node or None

        Key idea:
        Use a hash map to store the relationship between original nodes
        and their copied nodes.

        old_list_copy[original_node] = copied_node

        First pass creates all copied nodes.
        Second pass connects next and random pointers using the hash map.

        Time: O(n), because we visit each node twice.
        Space: O(n), because the hash map stores one copy for each original node.
        """
        cur = head
        # Adding None -> None lets us safely handle None random or next pointers
        old_list_copy = {None: None}

        # first pass: create a copy of the nodes, but don't connect
        while cur:
            copy = Node(cur.val)
            old_list_copy[cur] = copy
            cur = cur.next

        cur = head

        # second pass: Use hash map to connect each copied node's next and random pointers.
        while cur:
            copy = old_list_copy[cur]
            copy.next = old_list_copy[cur.next]
            copy.random = old_list_copy[cur.random]
            cur = cur.next
        return old_list_copy[head]
