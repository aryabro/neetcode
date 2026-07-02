# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = head
        count = 1
        while count < n:
            tail = tail.next
            count += 1
        prev = dummy
        while tail.next:
            tail = tail.next
            prev = prev.next
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        return dummy.next if head else prev

