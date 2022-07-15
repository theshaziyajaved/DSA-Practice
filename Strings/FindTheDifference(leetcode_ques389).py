class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        
        s.sort()
        t.sort()

        #since t is +1 of length of s we add an empty string ("") to s to avoid index out of range error
        s.append(" ")
        
        for i in range(len(t)):
            if (s[i] != t[i]):
                return t[i]
    