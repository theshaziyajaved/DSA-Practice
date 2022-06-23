
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
        
    temp=head
    if (k == 1):
        # temp=head
        head=temp.next
    
       
    temp = head
    prev = head
    count = 0
    
    while (temp != None):
        count += 1
        if (count == k):
            prev.next = temp.next
            break
        prev = temp
        temp = temp.next
    return head