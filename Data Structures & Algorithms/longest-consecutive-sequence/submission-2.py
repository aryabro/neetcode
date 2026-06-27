class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Pattern: Hash Set + sequence start detection.

        Possible approaches:
        1. Brute force:
           For every number, repeatedly search for the next consecutive number in nums.
           each lookup is O(n), giving O(n^2).
        2. Sorting:
           Sort nums, then count consecutive streaks in one pass.
           But sorting costs O(n log n).
        3. Hash set:
           Store all numbers in a set for O(1) average lookup. (costs O(n))
           Only start counting when num - 1 does not exist, meaning num is the
           beginning of a sequence. Then expand forward with num + 1.

        If num - 1 exists, then num is not the start of the sequence,
        so we skip it to avoid recounting the same streak.

        Time: O(n)
        Space: O(n), all unique numbers stored in a set.
        """
        nums_set = set(nums)
        max_length = 0
        # iterate unique numbers only
        for num in nums_set:
            length = 1
            # only find start of any sequence
            if num - 1 not in nums_set:
                while num+1 in nums_set:
                    length += 1
                    num += 1
            
            max_length = max(max_length, length)
        return max_length