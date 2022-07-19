from ast import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            if (i % 10 == nums[i]):
                return i
                break
            elif (i % 10 != nums[i]):
                i += 1
        return -1
        