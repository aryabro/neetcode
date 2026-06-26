class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Pattern: Prefix/Suffix accumulation. Can do in two passes, collect info while traversing.
        Possible approaches:
        1. Brute force: For every index, multiply all other elements.
           This works but is too slow: O(n^2).
        2. Division: Multiply all numbers, then divide by nums[i].
           Declined because the follow-up asks to solve without division, and zeros make it tricky.
           Will need 3 cases for 0 (if >2 zeroes, if 1 zero, if no zeroes)
        3. Prefix + Postfix products:
           Store the product of everything before i and multiply it by the product
           of everything after i.
        4. Same as 3. but store prefix and postfix array in output array for O(1) space complexity.

        Prefix idea:
            output[i] first stores product of all elements to the left of i.

        Postfix idea:
            Then we scan from right to left and multiply output[i] by product of
            all elements to the right of i.

        Example:
            nums = [a, b, c, d]

            prefix products for each index:
                [1, a, a*b, a*b*c]

            postfix products for each index:
                [b*c*d, c*d, d, 1]

            final answer:
                prefix[i] * postfix[i]

        This avoids division and also handles zeros naturally.

        Time: O(n)
        Space: O(1) extra space
        Note: output array does not count as extra space.
        """

        # Start with 1 because product identity is 1.
        # output[i] will first store product of all numbers before index i.
        output = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            # Store product of all elements to the left of i.
            output[i] = prefix

            # Update prefix to include current number for future indexes.
            prefix = prefix * nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            # Multiply left product already stored in output[i]
            # with product of all elements to the right of i.
            output[i] = output[i] * postfix

            # Update postfix to include current number for future indexes.
            postfix = postfix * nums[i]

        return output