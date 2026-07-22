from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = nums[0]
        for k,v in count.items():
            if v > count[res]:
                res = k
        return res