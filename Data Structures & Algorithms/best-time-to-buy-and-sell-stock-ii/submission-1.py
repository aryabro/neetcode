class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Pattern: Greedy / Array Traversal.

        Problem: Best Time to Buy and Sell Stock II
        - Can buy and sell stocks multiple times.
        - Can hold at most one stock at a time.
        - Goal: Maximize total profit.

        Approach: Greedy
        - Capture every positive price difference between consecutive days.
        - If today's price > yesterday's price, add the difference to profit.
        - No need to explicitly track buying and selling days.

        Example:
            prices = [7, 1, 5, 3, 6, 4]

            Buy at 1, sell at 5 -> profit = 4
            Buy at 3, sell at 6 -> profit = 3
            Total profit = 7

        Key Intuition:
        - Adding small consecutive profits is equivalent to
          buying at the lowest price and selling at the highest
          price within an increasing sequence.
        - Example: [1, 3, 5]
          (3 - 1) + (5 - 3) = 5 - 1 = 4

        Time: O(n) - Traverse the prices array once.
        Space: O(1) - Only store the total profit.
        """

        profit = 0

        # Start from day 1 to compare with the previous day's price.
        for i in range(1, len(prices)):

            # If price increased, capture the positive difference.
            if prices[i-1] < prices[i]:
                profit += (prices[i] - prices[i-1])

        # Return maximum profit from all profitable increases.
        return profit