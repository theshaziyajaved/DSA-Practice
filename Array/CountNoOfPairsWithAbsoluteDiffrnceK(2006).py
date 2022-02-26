from ast import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        
        for i in range (n):
            for j in range (i+1,n,1):
                if (abs(nums[i]-nums[j])==k):
                    count=count+1
        return count
            