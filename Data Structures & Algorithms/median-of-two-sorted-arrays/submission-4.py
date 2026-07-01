class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Pattern: Binary Search on Partition.

        Basically, divide both arrays such that both of their largest elements
        in the left half are smaller than or equal to both of their smallest 
        elements in the right half.

        This partition is valid when:
            maxLeftA <= minRightB
            maxLeftB <= minRightA
        
        Median calculation:
            if total len is odd:
                left partition of both arrays contain an 
                extra value, so it will be their max.
            if total len is even:
                median will be mid of (max(left partition), min(right partition))

        Time: O(log(min(m, n))), 
        Space: O(1)
        """
        # always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        a, b = nums1, nums2
        total = len(a) + len(b)
        mid = (total + 1) // 2

        # Number of elements we want on the combined left side.
        # For odd length, left side gets one extra element so the median
        # is simply max(left side).
        l, r = 0, len(a)

        while l <= r:
            # partition_a tells us where to cut array a
            # partition_b tells us where to cut array b
            partition_a = (l + r) // 2
            partition_b = mid - partition_a

            # Boundary values around partition_a.
            # If there is no left value, use -inf so it never blocks comparison.
            # If there is no right value, use inf so it never blocks comparison.
            maxLeftA = a[partition_a - 1] if partition_a > 0 else float("-inf")
            minRightA = a[partition_a] if partition_a < len(a) else float("inf")

            # Boundary values around partition_b.
            maxLeftB = b[partition_b - 1] if partition_b > 0 else float("-inf")
            minRightB = b[partition_b] if partition_b < len(b) else float("inf")

            # Correct partition:
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # Odd total length: left side has one extra element.
                if total % 2 == 1:
                    return max(maxLeftA, maxLeftB)

                # Even total length: median is average of the two middle values.
                return (
                    max(maxLeftA, maxLeftB) +
                    min(minRightA, minRightB)
                ) / 2

            # maxLeftA is too large, so we took too many elements from a.
            # Move partition_a left.
            elif maxLeftA > minRightB:
                r = partition_a - 1

            # maxLeftB is too large, so we did not take enough elements from a.
            # Move partition_a right.
            else:
                l = partition_a + 1