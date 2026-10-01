class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Pattern: Brute Force / String Divisibility.

        Approach:
        - The answer cannot be longer than the shorter input string.
        - Try candidate lengths from largest to smallest.
        - For each candidate length i:
            1. Both string lengths must be divisible by i.
            2. Take str1[:i] as the candidate substring.
            3. Repeat it enough times to check whether it forms
               both str1 and str2.
        - Since we check lengths from largest to smallest, the first
          valid candidate is the greatest common divisor string.

        Time: O(min(n1, n2) * (n1 + n2)) in the worst case,
              because we may test many candidate lengths and build/
              compare repeated strings.

        Space: O(n1 + n2) temporarily because repeated strings
               are created during validation.
        """

        n1, n2 = len(str1), len(str2)

        def isDivisor(i):
            # A substring of length i can only divide both strings
            # if i evenly divides both string lengths.
            if n1 % i != 0 or n2 % i != 0:
                return False

            # Number of times the candidate must repeat
            # to recreate each original string.
            f1, f2 = n1 // i, n2 // i

            # Use the first i characters of str1 as the candidate.
            # Check whether repeating it recreates BOTH strings.
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2

        # Start from the largest possible candidate length.
        # The first valid divisor we find is therefore the largest one.
        for i in range(min(n1, n2), 0, -1):
            if isDivisor(i):
                return str1[:i]

        return ""