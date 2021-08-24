# https://leetcode.com/problems/clone-graph/

def cloneGraph(self, node: 'Node') -> 'Node':
    # here the i/p node is the first node in graph
    
    # check if node exists
    if not node:
        return node
    
    # key is given node and value is the clone node created
    # Node is the class, initialise it by assigning val
    res = {node: Node(node.val)}
    
    # for DFS, using stack
    stack = [node]
    
    while stack:
        # n is node from stack
        n = stack.pop()
        
        # iterating through all neighbours of the current node
        for neigh in n.neighbors:
            # check if neigh's clone has been already created
            if neigh not in res:
                # appending it to stack for later iteration of its neighbors
                stack.append(neigh)
                # creating clone node
                # key is given node and value is the clone node created
                res[neigh] = Node(neigh.val)
                
            # appending newly created clone neighbours to the current clone node
            res[n].neighbors.append(res[neigh])
    
    # returning the first clone node
    return res[node]