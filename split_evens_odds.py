from singly_linked_list import SinglyLinkedList, Node

# develop a class that splits a linked list into two linked lists, one with the even values and one with the odd values
class SplitEvensOdds(SinglyLinkedList):

    def split_even_odd(self):
        if self.head is None:
            raise Exception("Cannot split an empty list")

        evens = SinglyLinkedList()
        odds = SinglyLinkedList()

        current = self.head

        self.head = self.tail = None
        self.count = 0

        while current:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if evens.tail is None:
                    evens.head = evens.tail = current
                else:
                    evens.tail.next = current
                    evens.tail = current
                evens.count += 1
            else:
                if odds.tail is None:
                    odds.head = odds.tail = current
                else:
                    odds.tail.next = current
                    odds.tail = current
                odds.count += 1

            current = next_node

        return evens, odds
