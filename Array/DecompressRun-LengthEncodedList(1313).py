from ast import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range (len(nums)//2):
            freq= nums[2*i]
            val= nums[2*i+1]
            arr += freq * [nums[2*i+1]]
        return arr
    
    
    