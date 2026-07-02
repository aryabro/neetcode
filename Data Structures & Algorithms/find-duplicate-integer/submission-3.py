class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Pattern: Floyd's Tortoise and Hare / Cycle Detection.

        We treat the array like a linked list:
        - Each index points to nums[index].
        - Since nums contains values from 1 to n, each value can be used
          as the next index.
        - The duplicate number creates a cycle because two indices point
          to the same value.

        Time: O(n), because each pointer moves through the array at most 
              a constant number of times.
        Space: O(1), because we only use pointers.
        """
        slow, fast = 0, 0

        # Phase 1: Detect a cycle.
        # slow moves one step: nums[slow]
        # fast moves two steps: nums[nums[fast]]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        finder = 0
        # Phase 2: Find the start of the cycle.
        # Move slow from the meeting point and finder from index 0.
        # Their meeting point is the duplicate value.
        while True:
            slow = nums[slow]
            finder = nums[finder]

            if slow == finder:
                return slow
