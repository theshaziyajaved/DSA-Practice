# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #using RECURSION
        ## Base cases
        if list1 == None and list2 == None:
            # both l1 and l2 are empty list
            return None
        
        elif not list1:
            # l1 is empty, directly return l2
            return list2
        
        elif not list2:
            # l2 is empty, directly return l1
            return list1
        
        ## General cases
        # Compare node value and merge
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        elif list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ITERATIVE APPROACH
        newlist = ListNoteBook()
        curr = newlist
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 != None:
            curr.next = list1
        else:
            curr.next = list2
        return newlist.next
        