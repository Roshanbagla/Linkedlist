"""Creating LinkedList."""

# create a node
# create a LinkedList
# insert node to LinkedList
# print LinkedList


class Node:
    """Created a Node."""

    def __init__(self, data):           # a node will have data and next field
        """Constructer function."""
        self.data = data
        self.next = None


class LinkedList:
    """Creaing a LinkedList."""

    def __init__(self):
        self.head = None

    def insert(self, newNode):
        """Inserting a new node to linkedlist."""
        if self.head is None:               # head -> John--> None
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        """Printing the LinkedList."""
        first_node = self.head
        while True:
            if first_node is None:
                break
            else:
                print(first_node.data)
            first_node = first_node.next


first_node = Node("John")        # creating a node object
linkedlist = LinkedList()       # created a linkedlist
linkedlist.insert(first_node)
second_node = Node("Ben")
linkedlist.insert(second_node)
third_node = Node("Rosh")
linkedlist.insert(third_node)
linkedlist.printList()
