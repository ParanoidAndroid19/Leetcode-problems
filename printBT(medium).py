# https://leetcode.com/problems/print-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[str]]
    """
    if root == None:
        return []
    
    # rows
    height = self.getHeight(root)
    # cols
    n = 2**(height) - 1
    
    # res = [[""]*n]*height
    res = [ [ "" for i in range(n) ] for j in range(height) ]
    
    # bfs
    # root pos
    c = int((n-1)/2)
    queue = deque()
    queue.append([root, 0, c])
    # res[0][c] = root.val
    bfs = []
    
    
    while len(queue) != 0:
        levelSize = len(queue)
        currentLevel = []
        
        for i in range(levelSize):
            current = queue.popleft()
            currentNode = current[0]
            currentLevel.append(currentNode)
            
            r = current[1]
            c = current[2]
            res[r][c] = str(currentNode.val)
            
            if currentNode.left != None:
                queue.append([currentNode.left, r+1, c-2**(height-r-2)])
            
            if currentNode.right != None:
                queue.append([currentNode.right, r+1, c+2**(height-r-2)])
                
        bfs.append(currentLevel)
        
    return res
            
    
def getHeight(self, root):
    if root == None:
        return 0
    
    return 1 + max(self.getHeight(root.left), self.getHeight(root.right))