class Solution:
    def truncateSentence(self, s: str, k: int) -> str:  
        n=len(s)
        string=""
        s=s.split()
        for i in range (n):
            if(i<k-1):
                string += s[i]
                string += " "
            
            elif (i==k):
                break
        string +=s[k-1]
        return string
        
        