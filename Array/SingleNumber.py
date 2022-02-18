from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<2):
            return nums[0]
        nums.sort()
        
        for i in range(0,n,2):
            if (n-i) < 2:
                return nums[-1]
            
            if (nums[i] != nums[i+1]):
                return nums[i]
        
        