#A single node of a singly linked list
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#Linked List with a single head node
class LinkedList:
    def __init__(self):
        self.head = None