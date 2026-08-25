class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Pattern: Dutch National Flag / Three Pointers.

        Goal:
        Sort an array containing only 0, 1, and 2 in-place.

        Pointer meaning:
        - l: next position where a 0 should go
        - i: current element being processed
        - r: next position where a 2 should go

        Array invariant (i.e. always stays true):
        - nums[0:l] contains only 0s
        - nums[l:i] contains only 1s
        - nums[i:r+1] is still unprocessed
        - nums[r+1:] contains only 2s

        Cases:
        1. nums[i] == 0:
           Swap it with nums[l].
           Increment both l and i because the left side is now finalized.

        2. nums[i] == 1:
           It is already in the correct middle section.
           Only increment i.

        3. nums[i] == 2:
           Swap it with nums[r] and decrement r.
           Do NOT increment i because the value swapped in from the right
           has not been processed yet.

        Time: O(n)
        Each element is processed a constant number of times.

        Space: O(1)
        Sorting is done in-place using only three pointers.
        """
        l, i, r = 0, 0, len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
        