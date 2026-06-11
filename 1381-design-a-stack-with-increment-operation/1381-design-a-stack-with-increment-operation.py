class CustomStack:

    def __init__(self, maxSize: int):
        self.st1=[]
        self.st2=[]
        self.maxSize=maxSize

    def push(self, x: int) -> None:
        if len(self.st1)!=self.maxSize:
            self.st1.append(x)

    def pop(self) -> int:
        if not self.st1:
            return -1
        return self.st1.pop()

    def increment(self, k: int, val: int) -> None:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        if not self.st1:
            r=0
            while self.st2 :
                if r<k:
                    self.st1.append(self.st2.pop()+val)
                    r+=1
                else:
                    self.st1.append(self.st2.pop())


        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)