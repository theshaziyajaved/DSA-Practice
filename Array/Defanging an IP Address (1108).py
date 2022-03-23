class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in address:
            str=address.replace(".", "[.]")
        return str
    
    
#replace() is an inbuilt function in Python that returns a copy of the string where all occurrences of a substring are replaced with another substring. 
 
#Syntax : string.replace(old, new, count)
#old – old substring you want to replace. 
#new – new substring which would replace the old substring.
#count – the number of times you want to replace the old substring with the new substring. (Optional ) 