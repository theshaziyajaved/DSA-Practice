from ast import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m=len(word1)
        n=len(word2)
        
        for i in range (m):
            a = ("".join(word1)) 
        
        for j in range (n):
            b = ("".join(word2))
        
        if (a==b):
            return (True)
        else:
            return (False)
        