def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 1
        while j <= len(nums)-1:
            ptr1 = nums[i]
            ptr2 = nums[j]
            if ptr1 == 0 and ptr2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif ptr1 == 0 and ptr2 ==0:
                j += 1
            else:
                i += 1
                j += 1
                continue
                
        return nums