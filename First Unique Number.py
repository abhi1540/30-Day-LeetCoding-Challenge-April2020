class FirstUnique:
    

    def __init__(self, nums: List[int]):
        
        
        self.dict1 = {}
        self.elements = []
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        while len(self.elements) > 0 and self.dict1[self.elements[0]] > 1:
            self.elements.pop(0)
        if len(self.elements) == 0:
            return -1
        else:
            return self.elements[0]

        

    def add(self, value: int) -> None:
        
        if value in self.dict1:
            self.dict1[value] += 1
            # print(self.dict1)
        else:
            self.dict1[value] = 1
            self.elements.append(value)
        #print(self.dict1)