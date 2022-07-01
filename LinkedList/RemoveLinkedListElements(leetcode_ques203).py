# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        dhead = ListNode()
        dhead.next = head
        prev = dhead
        
        while (temp != None):
            if(temp.val == val):
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return dhead.next
        