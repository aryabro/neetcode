class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        # res = nums + nums
        
        # res.extend(nums)
        # res.extend(nums)

        # res = nums.copy()
        # for n in nums:
        #     res.append(n)

        for _ in range(2):
            for n in nums:
                res.append(n)
        
        return res