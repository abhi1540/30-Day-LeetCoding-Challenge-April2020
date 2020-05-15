def maxSubArray(self, nums: List[int]) -> int:
        
        max_globe = max_curr = nums[0]
        
        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            
            if max_curr > max_globe:
                max_globe = max_curr
                
        return max_globe