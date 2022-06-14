def isLengthEvenOrOdd(head):
    # Code here
    temp = head
    count = 0
    while (temp is not None):
        count += 1
        temp = temp.next
   
    
    if (count%2==0):
       return 0
    else:
        return 1