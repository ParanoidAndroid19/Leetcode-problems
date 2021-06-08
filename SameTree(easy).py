# https://leetcode.com/problems/same-tree/

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(self, p, q):
    # base case, at the end of tree
    if p == None and q == None:
        return True
    
    if p and q:
        # for a tree to be equal, it's root should match and both left and right subtrees too
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
    