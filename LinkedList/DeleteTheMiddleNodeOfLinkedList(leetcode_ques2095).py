# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
        count=0
        temp = head
        
        while temp is not None:
            count += 1
            temp = temp.next
        # print(count)
        
        if count == 1:
            return head.next
        
        temp = head
        prev = head
        
        for i in range (0,count//2+1):
            if (i== count//2-1):
                prev.next = prev.next.next
            
            if (temp!= None):
                temp = temp.next
                prev = prev.next
        return head
        