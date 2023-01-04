class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Node sebelumnya belum ada")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def deletedlist(self, key):
        global prev
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None


if __name__ == "__main__":
    llist = linkedlist()
    llist.append(8)
    llist.push(9)
    llist.push(11)
    llist.append(25)
    llist.append(43)
    llist.insertAfter(llist.head.next, 62)

    print("Berikut adalah list-nya: ")
    llist.printlist()
    llist.deletedlist(25)
    print("\nlist setelah dihapus: ")
    llist.printlist()