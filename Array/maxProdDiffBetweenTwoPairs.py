from ast import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prod_of_max_vals = nums[-1] * nums[-2]
        prod_of_min_vals = nums[0] * nums[1]
        return prod_of_max_vals - prod_of_min_vals
        
        
        