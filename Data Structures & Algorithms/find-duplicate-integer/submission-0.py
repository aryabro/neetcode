class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                return n