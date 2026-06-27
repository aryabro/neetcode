class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0
        
        while l < r:
            # volume of container. h * l. b is constant.
            amount = min(heights[l], heights[r]) * (r - l)
            max_amount = max(max_amount, amount)

            # updating pointer by moving smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
    
        return max_amount
