class Solution:
    from collections import deque

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Pattern: Sliding Window + Monotonic Deque.

        Problem:
        Given an array nums and a window size k, return the maximum value
        in every contiguous window of size k.

        Key idea:
        We keep a deque of indices, not values. Think of indices as "timestamps" for expiration.
        
        - The deque stores indices whose values are in decreasing / non-increasing order.
        - Evict the weak: Smaller, older numbers are kicked out from right (they can never be the max).
        - Heirs to the throne: Smaller, newer numbers wait in line behind the current max.
        - Basically imagine a queue, a big number enters from back of queue(right) 
          and kicks out all numbers smaller than him.

        Time: O(n) Each index is added once and removed at most once.
        Space: O(k) The deque stores indices from the current window.
        """
        output = []
        q = deque()  # stores indices of useful elements in decreasing value order

        l = r = 0  # left and right boundaries of the sliding window

        while r < len(nums):
            # Remove smaller values from the back.
            # They are useless because nums[r] is bigger and more recent.
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index. The index acts like a timestamp for expiration.
            q.append(r)

            # Retire the old: If the leftmost index is outside the current window, remove it.
            if q[0] < l:
                q.popleft()

            # Once we have a full window of size k, record the max.
            if (r + 1) >= k:
                # Front of deque always holds index of max value in window.
                output.append(nums[q[0]])

                # Move left boundary forward to slide the window.
                l += 1

            # Always expand the right boundary.
            r += 1

        return output