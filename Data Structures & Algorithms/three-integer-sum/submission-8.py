class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Pattern: Sort + Two Pointers.
        Possible approaches:
        1. Brute force:
           Check every triplet using three loops.
           O(n^3) time.

        2. Hash set:
           Fix one number and solve the remaining problem like Two Sum using a set.
           O(n^2), but duplicate handling becomes more annoying and confusing.

        3. Sort + Two Pointers:
           Sort the array first. Then fix one number nums[i], and use two pointers
           to find two other numbers that sum to -nums[i].

           Since the array is sorted:
           - If the current sum is too small, move left pointer right.
           - If the current sum is too large, move right pointer left.

           We skip duplicate fixed values and duplicate pointer values so the answer
           does not contain repeated triplets.

        Time: O(n^2), because for each fixed i, left and right scan the rest once.
        Space: O(1) extra space, ignoring the output.
        """

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            # Skip duplicate fixed values to avoid duplicate triplets.
            # Example: [-1, -1, 0, 1], we only want to use the first -1 as fixed.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since nums is sorted, if fixed number is positive,
            # everything after it is also positive, so sum cannot be 0.
            if num > 0:
                break

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = num + nums[l] + nums[r]

                # Sum too large, reduce r
                if curr_sum > 0:
                    r -= 1

                # Sum too small, increase l
                elif curr_sum < 0:
                    l += 1

                else:
                    res.append([num, nums[l], nums[r]])
                    # Move both pointers
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res