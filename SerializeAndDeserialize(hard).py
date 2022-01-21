def serialize(self, root):
    
    def rserialize(root, string):
        # base case
        if(root is None):
            string = string + 'None,'

        else:
            string = string + str(root.val) + ','
            # dfs style
            string = rserialize(root.left, string)
            string = rserialize(root.right, string)

        return string

    return rserialize(root, '')



def deserialize(self, data):

    def rdeserialize(li):
        # none case
        if(li[0] == 'None'):
            li.pop(0)
            return None

        # creating node
        root = TreeNode(li[0])
        # popping the val just used to create node
        li.pop(0)

        # dfs style
        root.left = rdeserialize(li)
        root.right = rdeserialize(li)

        return root

    # converting data string to list
    data_list = data.split(',')
    root = rdeserialize(data_list)

