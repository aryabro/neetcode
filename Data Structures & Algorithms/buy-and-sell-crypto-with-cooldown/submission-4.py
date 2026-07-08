class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i:int, is_looking_to_buy:bool):
            # base case 1: if i crosses len(prices)
            if i >= len(prices):
                return 0

            # memo: if already in memo, return that value
            if (i, is_looking_to_buy) in memo:
                return memo[(i, is_looking_to_buy)]

            # we have two choices, either buy/sell or cooldown
            if is_looking_to_buy:
                profit_if_buy = dfs(i + 1, not is_looking_to_buy) - prices[i]
                profit_if_cooldown = dfs(i + 1, is_looking_to_buy)
                memo[(i, is_looking_to_buy)] = max(profit_if_buy, profit_if_cooldown)

            else:
                # remember i+2, NOT i+1, as we HAVE to take cooldown day
                profit_if_sell = dfs(i + 2, not is_looking_to_buy) + prices[i]
                profit_if_cooldown = dfs(i + 1, is_looking_to_buy)
                memo[(i, is_looking_to_buy)] = max(profit_if_sell, profit_if_cooldown)

            return memo[(i, is_looking_to_buy)]
            
        return dfs(0, True)