# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        
        while fast.next != None:
            slow = slow.next
            fast= fast.next
            
            if (fast.next != None):
                fast = fast.next
        return slow
    
    
        
        
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count=0
        temp = head
        
        while temp is not None:
            count += 1
            temp = temp.next
        # print(count)
        
        temp = head
        for i in range (0,count//2+1):
            if (i== count//2):
                return temp
            temp = temp.next
        return null
            
    
    