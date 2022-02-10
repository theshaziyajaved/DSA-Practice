from ast import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n=len(operations)
        count=0
        
        for i in range (n):
            if operations[i]== "--X":
                count=count-1
            elif operations[i]== "X--" :
                count=count-1
            elif operations[i]== "++X" :
                count=count+1
            else :
                count=count+1
                
        return count
        