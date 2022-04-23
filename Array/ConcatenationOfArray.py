from ast import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]*(2*n)
        
        for i in range(n):
            ans.append(nums[i])
        i=0
        for k in range(n):
            ans.append(nums[i])
            i=i+1
        return ans