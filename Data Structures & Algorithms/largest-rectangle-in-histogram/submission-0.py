class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Pattern: Monotonic Increasing Stack.
        Problem:
        Given a list of bar heights where each bar has width 1,
        return the area of the largest rectangle that can be formed
        inside the histogram.

        For each height, we want to know how far it can extend left and right.

        We maintain a stack of (start_index, height) pairs.
        The stack is increasing by height.

        - If the current height is greater than or equal to the stack top,
          it can safely be added because previous bars can still extend right.
        - If the current height is smaller than the stack top,
          the taller bar can no longer extend right, so we pop it
          and calculate its maximum possible rectangle area.

        The start_index helps us remember how far left the current height
        can extend after popping taller bars.

        Time: O(n), because each bar is pushed and popped at most once.
        Space: O(n), because the stack can store up to all bars.
        """        
        max_area = 0
        stack = [] # stores start_index and height

        for i, h in enumerate(heights):
            # Assume the current bar starts at its own index.
            # This may move left if we pop taller bars.
            start = i

            # If the current height (h) is < than the previous height (stack[-1][1]),
            # then the previous taller bar cannot extend past index i.            
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # The popped height started at `index` and ends right before i.
                max_area = max(max_area, height * (i - index))

                # Since current height h is smaller, it can extend backward
                # to the popped bar's start index.
                start = index
            
            # push current height with earliest index it can start from
            stack.append((start, h))

        # Any heights left in the stack were never blocked by a smaller bar,
        # so they can extend all the way to the end of the histogram.
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

