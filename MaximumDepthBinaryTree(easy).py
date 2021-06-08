# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root):
    if root == None:
        return 0

    # so first in and first out    
    queue = deque()
    # starting from root
    queue.append(root)

    maxDepth = 0

    while len(queue) != 0:
        levelSize = len(queue)

        maxDepth = maxDepth + 1

        for _ in range(levelSize):
            # getting it out of queue
            currentNode = queue.popleft()

            # kepping the current node's children in queue for future
            if(currentNode.left != None):
                queue.append(currentNode.left)
            if(currentNode.right != None):
                queue.append(currentNode.right)

    return maxDepth