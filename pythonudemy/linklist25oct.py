class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return 'added'

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode() #to increment to next node;

    def findNode(self, value):
        curr = self.head
        while curr:
            if curr.getData() == value:
                return True
            curr = curr.getNextNode()
        return False

    def removeNode(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:  #if curr value matched with the value
                if prev:
                    prev.setNextNode(curr.getNextNode()) #point prev to cur next
                else:
                    self.head = curr.getNextNode() #head points to cur's next eliminating curr
                    return True

            prev = curr  # prev changes to curr by increment by 1
            curr = curr.getNextNode() # curr increment by 1

        return False


myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")

print(myList.getSize())
print(myList.findNode(5))
print(myList.removeNode(25))

print("Printing")
myList.printNode()

