# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# my solution
# class Solution:
#     def __init__(self):
#         self.res = []
        
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def preOrder(root):
#             self.res.append(root)
            
#             if root.left != None:
#                 preOrder(root.left)
                
#             if root.right != None:
#                 preOrder(root.right)
                
        
#         preOrder(root)
        
#         if p.val < q.val:
#             s = p.val
#             l = q.val
#         else:
#             s = q.val
#             l = p.val
            
#         for num in self.res:
#             # if num lies b/w s and l
#             if(s <= num.val and num.val <= l):
#                 return num


# given, iterative approach
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    node = root
    
    # iterative approach works here because there is no need for backtracking
    while node != None:
        # both p and q in right subtree
        if p.val > node.val and q.val > node.val:
            node = node.right
            
        # both p and q are in left subtree
        elif p.val < node.val and q.val < node.val:
            node = node.left
            
        else:
            return node