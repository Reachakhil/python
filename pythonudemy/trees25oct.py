class  Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
