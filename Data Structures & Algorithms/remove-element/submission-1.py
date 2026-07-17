class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Pattern: Two Pointers / Swap with the Last Element.

        Goal:
        Remove every occurrence of `val` in-place and return the number of
        remaining elements.

        Key idea:
        The order of the remaining elements does not matter.

        We maintain two boundaries:
        - `i`: current index being inspected.
        - `n`: exclusive end of the valid, unprocessed portion of the array.

        When nums[i] == val:
        - Shrink the valid portion by moving `n` left.
        - Copy the last unprocessed element into index `i`.
        - Do not increment `i`, because the copied element has not been
          inspected yet.

        When nums[i] != val:
        - The element is valid, so move `i` forward.

        Time: O(n)
        Each element is inspected or moved at most a constant number of times.

        Space: O(1)
        The array is modified in-place without an additional data structure.

        This approach is especially useful when:
        - The order of the remaining elements does not matter.
        - `val` appears relatively few times, because it performs fewer writes
          than shifting every valid element forward.
        """

        # Current index being checked.
        i = 0

        # `n` represents the exclusive boundary of the valid search region.
        # Elements at indices n and beyond are considered removed.
        n = len(nums)

        while i < n:
            if nums[i] == val:
                # Remove nums[i] by shrinking the active array boundary.
                n -= 1

                # Replace the unwanted value with the last element
                # from the active portion of the array.
                nums[i] = nums[n]

                # Do not increment `i`.
                # The newly copied element at nums[i] still needs to be checked.
            else:
                # nums[i] should remain in the array, so inspect the next index.
                i += 1

        # Only nums[0:n] contains the remaining valid elements.
        return n