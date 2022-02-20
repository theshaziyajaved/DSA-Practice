from ast import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr=[]
        k=(num//3)
        sum=((k-1)+(k)+(k+1))
        if (sum==num):
            arr.append(k-1)
            arr.append(k)
            arr.append(k+1)
        return arr
        if (sum!=num):
            return arr
    
    
    
    