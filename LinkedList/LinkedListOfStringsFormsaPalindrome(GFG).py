
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    string = ""
    temp = head
    
    while (temp != None):
        string += str(temp.data)
        temp = temp.next
        
    new_s = string[::-1]
    
    if (string == new_s):
        return True
    else:
        return False