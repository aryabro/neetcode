class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Pattern: Two Pointers on a sorted array.
        Possible approaches:
        1. Brute force:
           Try every pair and check if numbers[i] + numbers[j] == target.
           Takes O(n^2) time.
        2. Binary search:
           For each number, search for target - numbers[i] in the remaining array.
           Works because the array is sorted, but takes O(n log n).
        3. Hash map:
           Store each number and its index while searching for the complement.
           Works in O(n), but uses O(n) extra space, which violates the O(1)
           extra space requirement.
        4. Two pointers:
           Since the array is sorted, place one pointer at the start and one
           pointer at the end.
           - If the current sum is too small, move left pointer right to increase sum.
           - If the current sum is too large, move right pointer left to decrease sum.

        Time: O(n), because each pointer moves at most n times.
        Space: O(1), because we only store two pointers.

        Note:
        The problem asks for 1-indexed positions, so return l + 1 and r + 1.
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]