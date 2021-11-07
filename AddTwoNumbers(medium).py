def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1 = self.reverse(l1)
    l2 = self.reverse(l2)
    
    num1 = ''
    num2 = ''
    
    p1 = l1
    p2 = l2
    
    while p1 != None:
        num1 = num1 + str(p1.val)
        p1 = p1.next
        
    while p2 != None:
        num2 = num2 + str(p2.val)
        p2 = p2.next
    
    temp = int(num1) + int(num2)
    res_num = str(temp)
    head = tail = ListNode(-1)
    
    for i in range(len(res_num)-1, -1, -1):
        tail.next = ListNode(int(res_num[i]))
        tail = tail.next
        
    return head.next
    

def reverse(self, head):
    node = head
    prev = None
    
    while node != None:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
        
    return prev