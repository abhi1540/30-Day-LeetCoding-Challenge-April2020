    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(len(prices)-1):
            ptr1 = prices[i]
            ptr2 = prices[i+1]
            if ptr2 > ptr1:
                profit += (ptr2-ptr1)
        return profit