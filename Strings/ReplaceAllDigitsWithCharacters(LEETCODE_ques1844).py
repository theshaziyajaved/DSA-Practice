class Solution:
    def replaceDigits(self, s: str) -> str:
        s_ = ""
        
        for i in range (len(s)):
            if (i%2==0):
                s_ += s[i]
                
            elif (i%2==1):
                s_ += chr(ord(s[i-1])+int(s[i]))    #The chr() function returns the                                      character that represents the specified unicode.
                           #The ord() function returns the number representing the                               unicode code of a specified character.
        return s_