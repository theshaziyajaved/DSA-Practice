from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        if (n<2):
            return nums[0]
        nums.sort()
        
        count=1
        x=nums[0]
        for i in range (1,n,1):
            if (nums[i]==x):
                    count=count+1
            elif (nums[i]!=x):
                x=nums[i]
                count=1
            if (count > n//2):
                return x