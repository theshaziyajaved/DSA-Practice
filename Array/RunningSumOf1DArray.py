from ast import List


class Solution:
    
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        
        runningSum=0
    
        
        for i in range (n):
            runningSum= runningSum+nums[i]
            ans.append(runningSum)
        return ans