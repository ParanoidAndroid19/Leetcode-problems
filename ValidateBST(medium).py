# https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res = []
        
    def isValidBST(self, root):
        # left - root - right
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            self.res.append(root.val)
            if root.right != None:
                inOrder(root.right)
                
                
        inOrder(root)
        
        for i in range(1, len(self.res)):
            # if left is greater than root
            if self.res[i-1] >= self.res[i]:
                return False
            
        return True
        