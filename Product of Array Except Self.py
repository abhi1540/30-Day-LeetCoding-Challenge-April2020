    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = [1 for i in range(len(nums))]
        
        temp = 1
        for i in range(len(nums)): 
            out[i] = temp 
            temp *= nums[i]
        
        temp1 = 1
        for i in range(len(nums) - 1, -1, -1):
            try:
                out[i] = temp1 * out[i]
                temp1 *= nums[i]
                
            except:
                pass
        return out
            