from ast import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1 = ord(s[0])    #The ord() function returns the number representing the                     unicode code of a specified character.


        row1 = int(s[1])
        col2 = ord(s[3])
        row2 = int(s[4])
        
        l = []

        for i in range (col1,col2+1):
            for j in range (row1,row2+1):
                l.append(chr(i)+str(j))
        return l
            
            
            
            
