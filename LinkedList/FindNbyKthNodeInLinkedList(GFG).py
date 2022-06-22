'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''
        
import math
def fractionalNodes(head,k):
        #add code here
        count = 0
        temp = head
        while (temp!= None):
            count += 1
            temp = temp.next
          
        val = math.ceil(count/k)
        temp = head
        curr = 0
        while (temp != None):
            curr +=1
            if (curr == val):
                res = temp
            temp = temp.next
        return res
        