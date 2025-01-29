class MinStack:

    def __init__(self):
        self.mini = []
        self.minis= []  

    def push(self, val: int) -> None:
        self.minis.append(val)
        val = min(val,self.mini[-1]if self.mini else val)
        self.mini.append(val)

    def pop(self) -> None:
        self.minis.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.minis[-1]

    def getMin(self) -> int:
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()