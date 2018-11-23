class Node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:
    def __init__(self):
        self.root=None;

    def insert(self,value):
        if self.root==None:
            self.root=Node(value);
        else:
            self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=Node(value);
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=Node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("value already in tree");

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.value))
            self._print_tree(cur_node.right_child);

tree1=binary_search_tree()
tree1.insert(5)
tree1.insert(3)
tree1.insert(2)
tree1.insert(16)
tree1.insert(8)
tree1.insert(8)
tree1.print_tree()


