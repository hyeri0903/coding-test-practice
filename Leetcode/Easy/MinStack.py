class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        return self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        min_val = min(self.st)
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
