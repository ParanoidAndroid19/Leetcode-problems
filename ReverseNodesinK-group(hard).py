# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(NK)
# Space Complexity: O(K)

class Solution(object):
    def __init__(self):
        # will store head and tail of k groups
        self.lists = []
        
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        
        count = 0
        # prev = dummy
        temp = node.next
        
        while node != None and temp != None:
            node = temp
            count = count + 1
            
            if count == 1:
                gpHead = node
                temp = node.next
            
            elif count == k:
                temp = node.next
                self.reverse(gpHead, node.next)
                gpHead = None
                count = 0
                
            else:
                temp = node.next
                
        for i in range(len(self.lists)):
            tail = self.lists[i][1]
            if i == len(self.lists)-1:
                tail.next = gpHead
            else:
                tail.next = self.lists[i+1][0]
                
        return self.lists[0][0]
    
    
    def reverse(self, head, tail):
        currNode = head
        prev = None
        
        while currNode != tail:
            temp = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = temp
            
        self.lists.append([prev, head])