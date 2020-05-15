class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0:
            return 0
        
        res = 0
        for i in range(32, -1, -1):
            
            if (m & (1 << i)) != (n & (1 << i)):
                break
            else:
                #power &= (1 << i)
                #print(i, (m & (1 << i)))
                res += (m & (1 << i))
            
        return res