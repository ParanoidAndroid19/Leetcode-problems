# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = -1
        self.res = []
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # since the tree is a BST (left node is always smaller than root, 
        # root is smaller than right node). So the resultant inOrder array
        # would be sorted. So inOrder traverse only till you reach kth element
        # then ans is kth element
        def inOrder(root):
            if self.ans == -1:
                if root.left != None:
                    inOrder(root.left)

                self.res.append(root.val)
                # to avoid traversing the whole tree is kth ele is already found
                if len(self.res) == k:
                    self.ans = self.res[-1]

                if root.right != None:
                    inOrder(root.right)
        
        inOrder(root)
        return self.ans