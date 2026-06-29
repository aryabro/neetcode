class MinStack:
    """
    Pattern: Stack + Auxiliary Min Stack.
    Problem:
    Design a stack that supports push, pop, top, and getMin in O(1) time.
    Key idea:
    Use two stacks:
    1. stack: Stores the actual values.
    2. min_stack: At each index, stores the minimum value seen in stack up to 
                  that same index.
    Time: O(1)
    Space: O(n), because we store an extra min value for each pushed value.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
