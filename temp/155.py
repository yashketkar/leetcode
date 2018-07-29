class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = 0
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
            self.minimum = x
        else:
            if x < self.minimum:
                self.minimum = x
            self.stack.append((x, self.minimum))
        return None

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        pop = self.stack.pop()
        if self.stack:
            self.minimum = self.stack[-1][1]
        return None

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
