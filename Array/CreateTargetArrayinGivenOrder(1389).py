from ast import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        #zip() helps in assigning two values based on two lists
        for i,j in zip(index,nums):
            target.insert(i,j)
        #we use the insert function to place the desired value at desired location

        return target
