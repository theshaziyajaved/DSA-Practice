from ast import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
#binary search
# Obviously, the PeakElement can be solved using binary search. The judgement is: whether nums[mid]> nums[mid+1].
# If true, the peak element must exist in the left half, and we can eliminate the right half; else the peak element must exist in the right half, we can eliminate the left half.

        lower_bound =0
        upper_bound = len(nums)-1
        
        while (lower_bound < upper_bound):
            mid = (lower_bound + upper_bound)//2
            if (nums[mid] < nums[mid+1]):
                lower_bound = mid+1
            elif (nums[mid] > nums[mid + 1]):
                upper_bound = mid
        return upper_bound
