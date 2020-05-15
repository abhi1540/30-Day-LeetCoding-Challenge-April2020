class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + ((right - left) // 2)
            
            # our focus is to find smallest element
            # if middle > right means smallest element is in right side 
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                

        start = left
        left = 0
        right = len(nums) - 1
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
            
        
        while left <= right:
            mid = left + ((right - left) // 2)
            
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

                    
                    
        return -1