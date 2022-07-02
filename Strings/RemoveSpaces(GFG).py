#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        new_s = ''.join(letter for letter in s if letter.isalnum())
        return new_s
