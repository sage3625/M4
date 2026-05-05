#Generate the linked list and node classes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
   
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def build_list_forward(self, values):
        for v in values:
            self.append(v)

    def build_list_backward(self, values):
        for v in values:
            self.prepend(v)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.count += 1

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1