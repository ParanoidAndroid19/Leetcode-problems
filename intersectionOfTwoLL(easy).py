# https://leetcode.com/problems/intersection-of-two-linked-lists/

def getIntersectionNode(headA, headB):        
    pA = headA
    pB = headB

    while pA != pB:
        if pA is None:
            pA = headB
        else:
            pA = pA.next
        
        if pB is None:
            pB = headA
        else:
            pB = pB.next

    return pA