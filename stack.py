# Stack implementation using a stack ADT
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow: cannot pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack underflow: cannot peek into empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
