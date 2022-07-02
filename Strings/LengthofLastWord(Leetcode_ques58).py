class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.split() 
        li = s.split()
        n = len(li)
        
        count = 0
        for i in (li[n-1]):
            count += 1
        return count
            
    
            
        