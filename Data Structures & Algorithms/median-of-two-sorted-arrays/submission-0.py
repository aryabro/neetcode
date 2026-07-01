class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        a, b = nums1, nums2
        total = len(a) + len(b)
        mid = (total + 1) // 2

        l, r = 0, len(a)

        while l <= r:
            partition_a = (l + r) // 2
            partition_b = mid - partition_a

            maxLeftA = float("-inf") if partition_a == 0 else a[partition_a - 1]
            minRightA = float("inf") if partition_a == len(a) else a[partition_a]

            maxLeftB = float("-inf") if partition_b == 0 else b[partition_b - 1]
            minRightB = float("inf") if partition_b == len(b) else b[partition_b]

            # Correct partition found
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if total % 2 == 1:
                    return max(maxLeftA, maxLeftB)

                return (
                    max(maxLeftA, maxLeftB) +
                    min(minRightA, minRightB)
                ) / 2

            # Took too many elements from a
            elif maxLeftA > minRightB:
                r = partition_a - 1

            # Took too few elements from a
            else:
                l = partition_a + 1