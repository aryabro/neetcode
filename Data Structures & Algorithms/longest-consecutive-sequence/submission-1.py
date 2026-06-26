class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            length = 1
            # find start of any sequence
            if num - 1 not in nums_set:
                while num+1 in nums_set:
                    length += 1
                    num += 1
            
            max_length = max(max_length, length)
        return max_length