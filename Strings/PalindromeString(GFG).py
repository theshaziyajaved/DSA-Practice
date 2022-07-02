#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		#used the concept of slicing of strings and returning the elements from the last index 
		#to get a reversed string
		new_S = S[::-1]
    
        if (S == new_S):
            return 1
        else:
            return 0
    