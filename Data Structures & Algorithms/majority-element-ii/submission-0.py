class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) / 3
        res = []

        occurences = {}
        for n in nums:
            occurences[n] = occurences.get(n, 0) + 1
        
        for k,v in occurences.items():
            if v > threshold:
                res.append(k)

        return res