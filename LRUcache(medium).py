class DLinkedNode():
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

# the most recently accessed key will be right after head
# the least recently accessed node will be the tail
        
class LRUCache():
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        # dummy nodes for head and tail
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        # establishing connection b/w head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.cache:
            return -1

        node = self.cache[key]
        
        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key not in self.cache:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node = self.cache[key]
            # update the value.
            node.value = value
            self._move_to_head(node)
            
            
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        
    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

        
    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        # remove the node from whereever it is in the list
        self._remove_node(node)
        # add the node after head
        self._add_node(node)

        
    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res