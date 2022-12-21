#A single node of a singly linked list
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#Linked List with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    #method for inserting into linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode