class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None

class Solution: 
    
    
    def deleteAlt(self, head):
        #add code here
        temp = head
        
        while (temp != None):
            if (temp.next != None):
                temp.next = temp.next.next
                temp = temp.next
            else:
                return head
                