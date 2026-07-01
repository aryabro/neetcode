class Solution:
    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            # mid is in the left sorted portion,
            # so the minimum must be to the right.
            if nums[mid] > nums[r]:
                l = mid + 1

            # mid could be the minimum,
            # so keep it in the search space.
            else:
                r = mid

        min_index = l # or r as l == r

        # Step 2: Decide which sorted half to binary search.
        if nums[min_index] <= target <= nums[len(nums) - 1]:
            return self.binary_search(nums, target, min_index, len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, min_index - 1)

        