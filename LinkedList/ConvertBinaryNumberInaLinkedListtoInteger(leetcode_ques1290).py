# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook


class Solution:
    def getDecimalValue(self, head: ListNoteBook) -> int:
        temp = head
        count = 0
        while temp!= None:
            count += 1
            temp = temp.next
        
        temp = head
        sum = 0
        while temp!= None:
            for i in range (count-1,-1,-1):
                sum += temp.val*(pow(2,i))
                temp = temp.next
            return sum