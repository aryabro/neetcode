# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        tail = dummy

        # Move tail n steps ahead so there is a gap of n nodes
        # between prev and tail.
        for _ in range(n):
            tail = tail.next

        # Move both pointers until tail reaches the last node.
        # Then prev will be right before the node we need to remove.
        while tail.next:
            prev = prev.next
            tail = tail.next

        # Remove prev.next by skipping it.
        node_to_remove = prev.next
        prev.next = node_to_remove.next
        node_to_remove.next = None

        return dummy.next

