class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sum = 0
        j = 0
        n = len(nums)
        m = max(nums)
        for i in range (k):
            sum += m
            m += 1
            j += 1
            if j==k:
                break
        return sum
