class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


x = LinkedList()
c = LinkedList()

x.add(10)
x.add(20)
x.add(30)

print("x: ")
x.display()