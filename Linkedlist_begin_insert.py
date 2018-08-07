"""Inserting at the start of LinkedList."""


class Node():
    """Creating a node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    """Creating a LinkedList."""
    def __init__(self):
        self.head = None

    def inserthead(self, newNode):
        """Inserting node at the start."""
        temp = self.head
        self.head = newNode
        self.head.next = temp
        del temp

    def insertEnd(self, newNode):
        """Inserting a new node at the end of a LinkedList."""
        if self.head is None:
            self.head = newNode
        else:
            while True:
                lastNode = self.head
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        """Printing the LinkedList."""
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            else:
                print(currentNode.data)
            currentNode = currentNode.next


first_node = Node("John")
linkedlist = LinkedList()
linkedlist.insertEnd(first_node)
second_node = Node("Ben")
linkedlist.insertEnd(second_node)
third_node = Node("Rosh")
linkedlist.inserthead(third_node)
linkedlist.printList()
