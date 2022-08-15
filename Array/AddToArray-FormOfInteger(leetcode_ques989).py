from ast import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sum = 0
        for i in num:
            sum = sum*10 + i
        
        sum = sum + k
        res = str(sum)
        return list(res)
        