class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        reach = 0
        curr = 0
        for i in range(len(nums)):
            
            if reach < i:
                return False
            
            curr = i + nums[i]
            
            if curr > reach:
                reach = curr

        return True
     