class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    """
    :type head: Node
    :rtype: Node
    """
    if head == None:
        return None
    
    # deepCopy will be returned, it will point to the head of the deep copy list
    # initializing the new list
    deepCopy = Node(head.val)
    
    # key is th original node and value is the newly created deep copy node
    # using dictionary to keep a track of nodes created, so that duplicates are not created
    d = {head: deepCopy}
    
    # two pointers, pointing to the start of the both lists
    currNode = head
    currDeep = deepCopy
    
    while currNode != None:
        # dealing with next
        # check if the corresponding node has already been created
        if currNode.next in d:
            currDeep.next = d[currNode.next]
        else:
            # checking this since trying to set val, to avoid error of null's val
            if currNode.next != None:
                currDeep.next = Node(currNode.next.val)
                d[currNode.next] = currDeep.next
            else:
                currDeep.next = None
        
        # dealing with random
        # check if the corresponding node has already been created
        if currNode.random in d:
            currDeep.random = d[currNode.random]
        else:
            # checking this since trying to set val, to avoid error of null's val
            if currNode.random != None:
                currDeep.random = Node(currNode.random.val)
                d[currNode.random] = currDeep.random
            else:
                currDeep.random = None
                
        # moving the pointers further in corresponding list
        currNode = currNode.next
        currDeep = currDeep.next
                
    return deepCopy