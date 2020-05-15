class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
        
        return self.data.append(x)
        

    def pop(self) -> None:
        
        del self.data[-1]
        

    def top(self) -> int:
        
        return self.data[-1]
        

    def getMin(self) -> int:
        
        min = self.data[0]
        
        for i in self.data:
            if i < min:
                min = i
        return min