# {
		# Node Class
	# 	class Node:
	# 	    def __init__(self, data):   # data -> value stored in node
	# 	        self.data = data
	# 	        self.next = None
	# }
class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        temp = curr_node
        temp.data = temp.next.data
        temp.next = temp.next.next