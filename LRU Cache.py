class LRUCache:
    

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.tracking = 0
        self.cache = {}
        self.lru = {}
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.lru[key] = self.tracking
            self.tracking += 1
            #print(self.lru)
            return self.cache[key] 
        return -1
        
    def put(self, key: int, value: int) -> None:
        
        if len(self.cache) >= self.capacity and key in self.cache:
            self.cache[key] = value
            self.lru[key] = self.tracking
        
        if len(self.cache) >= self.capacity and key not in self.cache:
            # get key of low tracking count
            index = sorted(self.lru.items(), key=lambda item: item[1])[0][0]
            
            # pop from both dict
            del self.cache[index]
            del self.lru[index]
            
        
            
            
        # put new value in dict
        self.cache[key] = value
        self.lru[key] = self.tracking
        self.tracking += 1
        #print(self.lru)
            