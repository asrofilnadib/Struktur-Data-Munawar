class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class circularlist(object):
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            self.last_node.next = self.head

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


if __name__ == "__main__":
    llist = circularlist()
    llist.append(3)
    llist.append(39)
    llist.append(13)
    llist.append(21)
    llist.append(10)
    llist.display()