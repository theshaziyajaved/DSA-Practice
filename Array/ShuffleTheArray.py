class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=len(nums)
        arr=[]
        for i in range (x//2):
            arr.append(nums[i])
            arr.append(nums[(x//2)+i])
        i=i+1
        return arr
    
            