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

    def delete_last(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            self.count = 0
            return
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        cur.next = None
        self.tail = cur
        self.count -= 1

    def delete_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.delete_first()
            return
        cur = self.head
        while cur.next and cur.next.data != value:
            cur = cur.next
        if cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            self.count -= 1

    def remove_all(self, value):
        while self.head and self.head.data == value:
            self.delete_first()
        cur = self.head
        while cur and cur.next:
            if cur.next.data == value:
                cur.next = cur.next.next
                self.count -= 1
            else:
                cur = cur.next
        if self.tail and self.tail.data == value:
            self.tail = cur

    def display_reverse_nr(self):
        stack = []
        cur = self.head
        while cur:
            stack.append(cur.data)
            cur = cur.next
        print("None <- " + " <- ".join(map(str, reversed(stack))) + " <- Head")

    def __str__(self):
        cur = self.head
        s = "Head -> "
        while cur:
            s += str(cur.data) + " -> "
            cur = cur.next
        return s + "None"
