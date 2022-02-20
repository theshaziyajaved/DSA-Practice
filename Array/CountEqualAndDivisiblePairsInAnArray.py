from ast import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        for i in range (n):
            for j in range (n):
                if (nums[i]==nums[j] and i<j and ((i*j)%k==0)):
                    count=count+1
        return count
            
        