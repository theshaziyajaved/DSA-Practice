from ast import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        
        for i in range (n):
            for j in range (1,n,1):
                if (nums[i]==nums[j] and i<j):
                    count=count+1
                    
                
        return count