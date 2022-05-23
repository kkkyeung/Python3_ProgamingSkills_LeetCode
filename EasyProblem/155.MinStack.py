class MinStack:

    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        if len(self.stack) > 1: self.stack.pop()

    def top(self):
        if len(self.stack) == 1: return None
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

# Runtime: 71 ms, faster than 72.37% of Python3 online submissions for Min Stack.
# Memory Usage: 18.7 MB, less than 7.56% of Python3 online submissions for Min Stack.
# https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution