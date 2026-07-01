# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        i = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                i.next = list1
                i = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                i.next = list2
                i = list2
                list2 = list2.next

        if list1:
            i.next = list1
        else:
            i.next = list2
            
        return dummy_node.next