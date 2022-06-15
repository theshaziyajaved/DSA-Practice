# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def areIdentical(head1, head2):
    # Code here
    
    temp1 = head1
    temp2 = head2
    
    while (temp1 != None and temp2 != None):
        if (temp1.data != temp2.data):
            return False
        
        temp1 = temp1.next
        temp2 = temp2.next
        
    return True
    
