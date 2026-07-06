class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def recursion(n):
            if n in memo:
                return memo[n]
            
            memo[n] = recursion(n-1) + recursion(n-2)
            return memo[n]
        
        return recursion(n)