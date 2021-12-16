class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        min = self.stack[0]
        for i in range(len(self.stack) - 1,0,-1):
            if self.stack[i] < min:
                min = self.stack[i]
        return min


obj = MinStack()
obj.push(5)
obj.push(67)
obj.push(6)
obj.push(543)


param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,param_4)