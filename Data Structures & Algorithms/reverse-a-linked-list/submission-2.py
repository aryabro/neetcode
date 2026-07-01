# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # save next node in temp to prevent its loss
            # due to removing curr.next pointer
            temp = curr.next
            # reverse .next for current
            curr.next = prev

            # curr is reversed now
            # Update prev pointer
            prev = curr
            # Update curr pointer
            curr = temp
            
        head = prev
        return head