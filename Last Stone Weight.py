class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        

        
        x = sorted(stones, reverse = True)
        while len(x) > 1:
            x = sorted(x, reverse = True)
            print(x)
            fir, sec = x[0], x[1]
            if fir == sec:
                del x[0]
                del x[0]
            else:
                x.append(abs(x[0]-x[1]))
                
                del x[0]
                del x[0]
            
        if len(x) == 0:
            return 0
        else:
            return x[0]
            