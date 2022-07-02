class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        #using isalnum() function along with the string join() function to create a string with only alphanumeric characters
        new_s = ''.join(letter for letter in s if letter.isalnum())
        
        str = new_s[::-1]
        
        if (new_s == str):
            return True
        else:
            return False
        