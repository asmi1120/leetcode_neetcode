class MinStack:

    def __init__(self):
        self.st1=[]
        self.minst=[]

    def push(self, value: int) -> None:
        self.st1.append(value)
        if not self.minst:
            self.minst.append(value)
        else:
            self.minst.append(min(value,self.minst[-1]))

    def pop(self) -> None:
        self.st1.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.st1[-1]
        
    def getMin(self) -> int:
        return self.minst[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()