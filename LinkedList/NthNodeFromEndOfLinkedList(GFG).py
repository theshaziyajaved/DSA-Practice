#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    temp = head
    count = 0
    while (temp!=None):
        count += 1
        temp = temp.next
    
    temp= head
    if ((count-n) == 0):
        return temp.data
    if ((count-n) < 0):
        return -1
        
    val = count-n
    temp=head
    curr = 0
    while (temp!=None and val>0):
        curr += 1
        if (curr == val):
            # temp = temp.next
            return temp.next.data
            break
        temp = temp.next
    