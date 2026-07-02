# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Pattern: Linked List + Divide and Conquer.
    Problem:
    Given k sorted linked lists, merge them into one sorted linked list.

    Possible approaches:
    1. Brute force:
        Collect all node values into an array, sort the array, then build a new linked list.
        Time: O(N log N), where N is the total number of nodes.
        Space: O(N), because we store all values and create a new list.

    2. Heap / Priority Queue:
        Push the head of each list into a min heap.
        Repeatedly pop the smallest node and push its next node.
        Time: O(N log k), where k is the number of lists.
        Space: O(k), because the heap stores at most one node from each list.

    3. Recursion / Divide and Conquer:
        Recursively split the list of linked lists into halves.
        Merge the left half and right half, then merge those two results.
        Time: O(N log k)
        Space: O(log k), because of recursion call stack.

    4. Iterative Divide and Conquer:
        Merge lists in pairs until only one list remains.
        This avoids recursion and keeps merging balanced.
        This is the approach used below.

    Time: O(N log k), where:
            N = total number of nodes across all lists
            k = number of linked lists
    Space: O(1) extra space if we ignore the output list,
            because we reuse the existing linked list nodes.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: no lists were given.
        if not lists or len(lists) == 0:
            return None
        
        # keep merging in pairs and replace "lists" until only one list remains
        while len(lists) > 1:
            # lists        = current round of lists to merge
            # merged_lists = next round after merging pairs
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                # deals with odd number of lists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None 

                merged_lists.append(self.merge_two_lists(l1, l2))

            # After one full pass, replace lists with the newly merged lists.
            # Example: 8 lists -> 4 lists -> 2 lists -> 1 list.
            lists = merged_lists
        return lists[0]

    def merge_two_lists(self, l1, l2):
        """
        Helper Function (same as leetcode 21: Merge Two Sorted Lists)
        Time: O(m + n), where m and n are the lengths of l1 and l2.
        Space: O(1), because we reuse existing nodes.
        """
        dummy = ListNode()

        # tail always points to the last node in the merged list.
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
