class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Pattern: Dynamic Programming with memoized DFS.

        Problem:
        Given a list of stock prices, return the maximum profit you can make.
        You may complete as many transactions as you want, but after selling,
        you must wait one day before buying again.

        Key idea:
        At each day i, our decision depends on whether we are currently allowed
        to buy or whether we are holding a stock and looking to sell.

        dfs(i, is_looking_to_buy) returns the maximum profit we can make starting
        from day i with the current state:
        - is_looking_to_buy == True:
          We do not currently own a stock, so we can either buy or skip.
        - is_looking_to_buy == False:
          We currently own a stock, so we can either sell or skip.

        Choices:
        1. If looking to buy:
           - Buy today: lose prices[i], move to selling state tomorrow.
           - Cooldown/skip today: stay in buying state tomorrow.

        2. If looking to sell:
           - Sell today: gain prices[i], move to buying state after one cooldown day.
           - Cooldown/skip today: stay in selling state tomorrow.

        The cooldown rule is handled by jumping from i to i + 2 after selling.

        Time: O(n), because there are only 2 states per day.
        Space: O(n), because memo stores results for each state.
        """
        memo = {}

        def dfs(i:int, is_looking_to_buy:bool):
            # base case 1: if i crosses len(prices)
            if i >= len(prices):
                return 0

            # memo: if already in memo, return that value
            if (i, is_looking_to_buy) in memo:
                return memo[(i, is_looking_to_buy)]

            # Case 1:
            # We do not currently own a stock, so we are allowed to buy.
            if is_looking_to_buy:
                profit_if_buy = dfs(i + 1, not is_looking_to_buy) - prices[i]
                profit_if_cooldown = dfs(i + 1, is_looking_to_buy)
                memo[(i, is_looking_to_buy)] = max(profit_if_buy, profit_if_cooldown)

            # Case 2:
            # We currently own a stock, so we are allowed to sell.
            else:
                # remember i+2, as we HAVE to take cooldown day, so skip next day
                profit_if_sell = dfs(i + 2, not is_looking_to_buy) + prices[i]
                profit_if_cooldown = dfs(i + 1, is_looking_to_buy)
                memo[(i, is_looking_to_buy)] = max(profit_if_sell, profit_if_cooldown)

            return memo[(i, is_looking_to_buy)]
            
        return dfs(0, True)