class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Pattern: Binary Search on Rotated Sorted Array.
        Problem:
        Given a sorted array that was rotated, find the minimum element.
        Key idea:
        In a rotated sorted array, the minimum element is the "pivot point".

        We compare nums[mid] with nums[r] to decide which half contains the minimum.
        - If nums[mid] > nums[r]:
          mid is in the left sorted portion.
          The minimum must be to the right of mid.
        - Else nums[mid] <= nums[r]:
          mid is in the right sorted portion, or mid itself could be the minimum.
          So keep mid in the search space by doing r = mid.
        Time: O(log n)
        Space: O(1)
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # If mid is greater than the rightmost value,
            # then mid belongs to the left sorted portion.
            # Minimum must be somewhere to the right of mid.
            if nums[mid] > nums[r]:
                l = mid + 1

            # Otherwise, mid could be the minimum,
            # or the minimum is somewhere to the left of mid.
            # Keep mid in the search space.            
            else:
                r = mid
        # when l == r, it's the minimum element
        return nums[l]