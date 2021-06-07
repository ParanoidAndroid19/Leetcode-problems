# https://leetcode.com/problems/merge-two-sorted-lists/

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:        
    # dummy node
    dummy = temp = ListNode('D')
    
    while l1 != None and l2 != None:
        # checking for smallest
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        
        else:
            temp.next = l2
            l2 = l2.next
        
        # to keep temp pointer at the end of res LL
        temp = temp.next
    
    # handles edge case of both LL are empty or only 1 is empty
    # Also in case traversal of l1 is complete but not for l2
    temp.next = l1 or l2
    
    return dummy.next