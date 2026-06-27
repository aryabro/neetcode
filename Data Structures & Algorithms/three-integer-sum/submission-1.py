class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums) - 1
            while l < r:
                curr_sum = num + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    temp = tuple([num, nums[l], nums[r]])
                    if temp not in res:
                        res.add(temp)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[l] == nums[l-1]:
                        r -= 1
        return list(res)