class Node:

    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        super().__init__()
        self.head = None

    def sorted_insert(self, new_node):

        # Special case for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

            # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:

            # Locate the node before the point of insertion
            current = self.head
            while (current.next is not None and
                   current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Utility function to prit the linked LinkedList

    def printList(self):
        temp = self.head
        while (temp):
            print
            temp.data,
            temp = temp.next


if __name__ == '__main__':
    # Driver program
    llist = LinkedList()
    new_node = Node(5)
    llist.sorted_insert(new_node)
    new_node = Node(10)
    llist.sorted_insert(new_node)
    new_node = Node(7)
    llist.sorted_insert(new_node)
    new_node = Node(3)
    llist.sorted_insert(new_node)
    new_node = Node(1)
    llist.sorted_insert(new_node)
    new_node = Node(9)
    llist.sorted_insert(new_node)
    print
    "Create Linked List"
    llist.printList()
