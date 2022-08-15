from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        
        if len(nums)!=len(res):
            return True
        else:
            return False
        
        
        


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using sorting
         nums.sort()
         for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
         return False 



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Applying hashtable O(n)
        hashNum = {}
        for i in nums:
            if i not in hashNum:
                hashNum[i] = 1
            else:
                return True
        return False
    