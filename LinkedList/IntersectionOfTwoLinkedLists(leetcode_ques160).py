class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if (headA == None or headB == None):
            return None
        
        dhead1 = headA
        dhead2 = headB
        
        while (dhead1 != dhead2):
            # if either pointer hits the end, switch head and continue the second                       traversal 
            # if they do not hit the end, just move on to next
            if dhead1 == None:
                dhead1 = headB
            else:
                dhead1 = dhead1.next
            if dhead2 == None:
                dhead2 = headA
            else:
                dhead2 = dhead2.next
                
        return dhead1
              
# only 2 ways to get out of the loop, either they meet or they both hit the end i.e. None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, dhead1 or dhead2 would be the node we are looking for
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them i.e None
        