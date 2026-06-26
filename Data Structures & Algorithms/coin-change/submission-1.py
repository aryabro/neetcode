class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Possible approaches:
        1. Greedy does not work as it fails for non-canonical coin sets.
        2. Recursion is brute force.
        3. Top Down DP (DFS) is optimized version of Brute. As we calculate each value, 
        we store them in dict(dp).

        Bottom-up DP approach:

        dp[a] = minimum number of coins needed to make amount a.

        For every amount from 1 to target, try every coin.
        If coin c can be used, then the answer for amount a could be:
            1 coin c + best answer for remaining amount a - c

        Recurrence:
            dp[a] = min(dp[a], 1 + dp[a - c])

        We use amount + 1 as a fake "infinity" value because the answer can never
        need more than amount coins if coin 1 exists.

        Time: O(amount * len(coins))
        Space: O(amount)
        """        
        # Initialize every amount as unreachable at first.
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0.
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                # Only use coin c if it does not make the remaining amount negative.
                if a - c >= 0:
                    # Try taking coin c, then use the best known answer for a - c.
                    dp[a] = min(1 + dp[a - c], dp[a])

        # If dp[amount] was updated, amount is reachable.
        if dp[amount] != amount + 1:
            return dp[amount]

        # Otherwise, no combination of coins can make the target amount.
        else:
            return -1