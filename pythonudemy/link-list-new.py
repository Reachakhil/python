class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None   #next variable created here

class linked_list:
    def __init__(self):
        self.head=Node()  #to create a head

    def append(self,data):
        new_node=Node(data); #a new node with a data
        cur=self.head;   #cur to iterate over
        while cur.next!=None:  #till cur of next is null
            cur=cur.next;      #increment over
        cur.next=new_node;  #cur will point tonode created
    def length(self):
        cur=self.head;
        total=0;
        while cur.next!=None:
            total+=1;
            cur=cur.next;
        return total

    def display(self):
        ele=[]
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next;
            ele.append(cur_node.data);
        print(ele)

    def get(self, index):
        if index >= self.length():
            print("index out of error");
            return None
        cur_index=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_index==index:
                return cur_node.data;
            else:
                cur_index+=1

    def delete(self,index):
        if index >= self.length():
            print("out of index");
            return
        cur_index = 0;
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node==index:
                last_node.next = cur_node.next;
                return
            cur_index+=1;

list1 = linked_list()

list1.append(2);
list1.append(3);
list1.append(4);
x=list1.length();
print(x);
print(f"the ele at 1st position is{list1.get(1)}");
list1.delete(1);
list1.display();


