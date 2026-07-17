class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums

        # res = nums.copy()
        # for num in nums:
        #     res.append(num)
        # return res
        
        res = []
        for _ in range(2):
            for num in nums:
                res.append(num)
        return res