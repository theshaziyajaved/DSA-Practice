'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,node):
        #code here
        temp = node
        
        while (temp != None):
            print (temp.data,end=" ")
            temp = temp.next
        
            