class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l is index of min price seen so far
        # r is index of max price seen so far
        l = 0
        r = l
        max_profit = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            
            else:
                l = r
            r += 1
        return max_profit

        
        