class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i , j = 0,0
        count =0
        while i < len(s) and j < len(t):   # Loops till any of the strings is fully traversed
                if s[i] == t[j]:
                    i += 1
                    count += 1
                j += 1
         
        return (count == len(s))  #return True if count== len(s), else False
        