from ast import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[]
        n=len(candies)
        count = 0
        for i in range (n):
            count=0
            for j in range (n):
                if ((candies[i]+ extraCandies >= candies[j]) and i!=j):
                    count=count+1
                
            
            if (count==(n-1)):
                arr.append(True)
            else:
                arr.append(False)
        return arr 
    