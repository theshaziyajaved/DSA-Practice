class Solution:
    def balancedStringSplit(self, s: str) -> int:
      
        counter = 0
        output = 0
        for char in s:
            if char == "R":
                counter += 1 

            if char == "L":
                counter -= 1 
                
            if counter == 0:
                output += 1
        return output
        
        
        
        