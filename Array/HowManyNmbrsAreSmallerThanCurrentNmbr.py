from ast import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        n=len(nums)
        arr=[]
        for i in range (n):
            count=0
            for j in range (n):
                if (nums[i]>nums[j] and j!=i):
                    count=count+1
            arr.append(count)
        
        return arr
                    
        