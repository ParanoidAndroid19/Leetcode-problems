class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Solution 1: Two pass
def removeNthFromEnd(head, n):
    if head.next == None:
        return None

    current = head
    length = -1

    # calculate length
    while current != None:
        length = length + 1
        current = current.next

    target = length - n

    if target == -1:
        head = head.next
        return head

    node = head
    i = -1
    while node != None:
        i = i + 1

        if i == target:
            node.next = node.next.next
            return head

        node = node.next



# Solution 2: One pass, fast and slow pointers approach
def removeNthFromEnd(head, n):
    if head.next == None:
            return None
    
    # adding a "dummy" node, which points to the list head. 
    # The "dummy" node is used to simplify some corner cases such as a 
    # list with only one node, or removing the head of the list. 
    dummy = ListNode('D')
    dummy.next = head

    slow = fast = dummy
    i = 0

    while fast != None:
        i = i + 1

        # Moving fast pointer so that gap b/w slow and fast pointer is 
        # n nodes apart 
        if i <= n + 1:
            fast = fast.next

        # After there is n nodes gap b/w fast and slow
        else:
            slow = slow.next
            fast = fast.next


    slow.next = slow.next.next
    return dummy.next