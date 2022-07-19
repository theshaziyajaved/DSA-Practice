class Solution:
    def countAsterisks(self, s: str) -> int:
        if "|" not in s and "*" in s:
            return (s.count("*"))
        
        flag = False
        count = 0
        
        for ele in s :
            if (flag == False) and (ele == "|") :
                flag = True
                
            elif (flag == True) and (ele == "|") :
                flag = False
                
            if (flag == False) and (ele == "*") :
                count += 1
           
        return count
                
        