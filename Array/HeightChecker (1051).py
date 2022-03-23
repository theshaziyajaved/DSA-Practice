from ast import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m=len(heights)
        expected = list(heights)
        expected.sort()
        count=0
        for j in range (m):
            if (heights[j]!=expected[j]):
                count=count+1
            else:
                pass
        return count