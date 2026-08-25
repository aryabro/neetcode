class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        occ = {k:v for k,v in sorted(Counter(nums).items())}
        i = 0

        for k in occ:
            while occ[k] > 0:
                nums[i] = k
                occ[k] -= 1
                i += 1

