class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum = 0
        dict1 = {0:1}
        count = 0
        for i in nums:
            sum += i
            if (sum - k) in dict1:
                count += dict1[sum -k]
            if sum in dict1:
                dict1[sum] += 1
            else:
                dict1[sum] = 1
            
        return count