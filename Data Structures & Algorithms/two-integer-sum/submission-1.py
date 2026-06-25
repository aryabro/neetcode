class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen_nums.keys():
                return [seen_nums[complement], i]
            else:
                seen_nums[nums[i]] = i