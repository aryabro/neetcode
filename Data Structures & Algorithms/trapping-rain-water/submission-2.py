class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water = 0
        while l < r:
            if l_max <= r_max:
                if l_max > height[l]:
                    water += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                if r_max > height[r]:
                    water += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return water