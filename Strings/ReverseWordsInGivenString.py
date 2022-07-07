
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        res = S.split(".")
        s = " "
        n = len(res)
        for i in range (n-1,0,-1):
            s += res[i] + "."
        s += res[0]
        return (s.lstrip())
  

        
