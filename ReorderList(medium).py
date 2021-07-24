# https://leetcode.com/problems/reorder-list/

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    
    if not head:
        # Quick response for empty linked list
        return None
    
    # ----------------Step1--------------------------
    # Locate the mid point of linked list
    # First half is the linked list before mid point
    # Second half is the linked list after mid point
    
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow
    
    # ----------------Step2--------------------------
    # Reverse second half
    
    prev = None
    cur = mid
    
    while cur != None:
        temp = cur.next
        
        cur.next = prev
        
        prev = cur
        cur = temp
        
    secondHalf_head = prev
    
    
    # ----------------Step3--------------------------
    # Update link (next) between first half and reversed second half
    
    first = head
    second = secondHalf_head
    
    while second.next:
        # for first
        next_hop = first.next
        first.next = second
        first = next_hop
        
        # for second
        next_hop = second.next
        second.next = first
        second = next_hop


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

reorderList(head)