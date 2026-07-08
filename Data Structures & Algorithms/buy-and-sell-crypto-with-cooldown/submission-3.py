class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        # we update memo with profit at current i and is_looking_to_buy state
        def dfs(i:int, is_looking_to_buy:bool):
            # base case 1: if i crosses len(prices)
            if i >= len(prices):
                return 0

            # memo: if already in memo, return that value
            if (i, is_looking_to_buy) in memo:
                return memo[(i, is_looking_to_buy)]

            # we have two choices, either buy/sell or cooldown
            if is_looking_to_buy:
                buy = dfs(i + 1, not is_looking_to_buy) - prices[i]
                cooldown = dfs(i + 1, is_looking_to_buy)
                memo[(i, is_looking_to_buy)] = max(buy, cooldown)

            else:
                # remember i+2, NOT i+1, as we HAVE to take cooldown day
                sell = dfs(i + 2, not is_looking_to_buy) + prices[i]
                cooldown = dfs(i + 1, is_looking_to_buy)
                memo[(i, is_looking_to_buy)] = max(sell, cooldown)

            return memo[(i, is_looking_to_buy)]
            
        return dfs(0, True)