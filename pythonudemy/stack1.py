class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item);
    def pop(self):
         return self.items.pop();
    def isempty(self):
        if self.items==[]:
            return True;
    def printit(self):
        print(self.items);
    def lengthof(self):
        return len(self.items);

print('stack operations');
s1=Stack();
print("provide the max length of stack: ");
length=int(input());

x=int(input("enter the first digit to initiate stack:"));
s1.push(x);
print("menu:\n");
print("1----------push");
print("2----------pop");
print("3----------quit")

while True:
    print("enter choice::");
    l=int(input());
    if l==1:

        x = int(input("enter the digit to push:"));
        if(s1.lengthof()>=length):
            print("stack overflow");

        else:
            s1.push(x);
            s1.printit();
    elif l==2:
        if (s1.lengthof() == 0):
            print("your stack is empty,enter new item")
        else:
            s1.pop();
            s1.printit();
    elif l==3:
        break;

    else:
        print("wrong option , enter 1 for push,2 for pop,3 for printing stack");



