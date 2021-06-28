def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
    def array_to_tree(left, right):
        nonlocal preorder_index
        
        if left > right:
            return None
        
        # getting root
        root_value = preorder[preorder_index]
        root = TreeNode(root_value)
        
        preorder_index = preorder_index + 1
        
        # left and right subtree
        # left side of root in inorder array is left subtree
        # right side of root in inorder array is right subtree
        root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
        root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
        
        return root
        
    
    # to keep a track of root in preorder array
    preorder_index = 0
    
    # hashmap to store value: index, for inorder array, so that root's index 
    # can be found in O(1) time
    inorder_index_map = {}
    for i in range(len(inorder)):
        inorder_index_map[inorder[i]] = i
        
    # left and right are pointers to start and end of inorder array
    return array_to_tree(0, len(preorder)-1)