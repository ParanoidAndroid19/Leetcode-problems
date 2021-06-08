# https://leetcode.com/problems/subtree-of-another-tree/

def isSubtree(self, root, subRoot):
    # if we reach end of tree
    if root == None:
        return False
    
    # check if root's tree matches subRoot's tree
    if self.isSameTree(root, subRoot):
        return True
    
    # here we try all nodes in the tree, to see if it's tree matches with subRoot's tree
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def isSameTree(self, p, q):
    # base condition
    if p == None and q == None:
        return True
    
    if p and q:
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False