class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node


t=BinaryTree(3)
print(t.value)
print(t.left)