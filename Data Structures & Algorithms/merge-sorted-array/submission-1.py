class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Pattern: Two Pointers from the End.
        Problem:
        Merge two sorted arrays nums1 and nums2 into nums1 in-place.

        Key idea:
        nums1 has extra empty space at the end, so we fill nums1 from
        right to left. This prevents overwriting useful nums1 values.

        Possible approaches:
        1. Extra array:
           Merge both arrays into a new list, then copy it back into nums1.
           Works, but uses O(m + n) extra space.
        2. Insert nums2 into nums1 and sort:
           Copy nums2 into the empty slots of nums1, then sort nums1.
           O((m + n) log(m + n)) time.
        3. Two pointers from the end:
           Compare the largest remaining values from nums1 and nums2.
           Place the larger one at the last available position in nums1.

        Time: O(m + n), because each element is placed at most once.
        Space: O(1)
        """
        i = m - 1
        j = n - 1

        # "last" is placed at end of nums1 as extra space is provided
        last = m + n - 1

        # only check nums2 as if its empty, everything is sorted
        while j >= 0:
            # put the larger element at place of "last"
            
            # We travel from right to left, as inserting in-place
            # and extra space in the end
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1