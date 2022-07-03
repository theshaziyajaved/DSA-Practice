# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ""
        temp = head
        while (temp != None):
            string += str(temp.val)
            temp = temp.next
            
        new_string = string[::-1]
        
        if (string == new_string):
            return True
        else:
            return False
        