"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
def getNth(head, k):
    # Code here
    temp = head
    count = 0
    
    while (temp != None):
        count +=1
        if (count == k):
            return temp.data
        else:
            temp = temp.next
        
