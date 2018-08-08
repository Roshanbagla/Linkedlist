"""deleting the last element in the LinkedList."""


class Node():
    """Creating a node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    """Creating Linkedlist."""

    def __init__(self):
        self.head = None

    def deleteEnd(self):
        """Deleting a node at the end."""
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def insertEnd(self, newNode):
        """Inserting a new node at the end of the linkedlist."""
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head    # start traversing the list
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newNode

    def insertHead(self, newNode):
        """Inserting at the head of the linkedlist."""
        temp = self.head
        self.head = newNode
        self.head.next = temp
        del temp

    """def insertAt(self, newNode, position):
        Inserting a node in between the linkedlist.
        currentNode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                currentposition = +1"""

    def printList(self):
        """Printing linkedlist elements."""
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            else:
                print(currentNode.data)
                currentNode = currentNode.next


first_node = Node(10)
linkedlist = LinkedList()
linkedlist.insertEnd(first_node)
second_node = Node(20)
linkedlist.insertEnd(second_node)
third_node = Node(30)
fourth_node = Node(50)
linkedlist.insertEnd(third_node)
linkedlist.insertHead(fourth_node)
#linkedlist.insertAt(fifth_node, 2)
linkedlist.deleteEnd()
linkedlist.printList()
