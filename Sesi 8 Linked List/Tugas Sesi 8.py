class Node(object):
    def __init__(self, no_buku=None, nama_buku=None, harga_buku=None):
        self.no_buku = no_buku
        self.nama_buku = nama_buku
        self.harga_buku = harga_buku
        self.next = None


class sllc(object):
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, no_buku, nama_buku, harga_buku):
        if self.last_node is None:
            self.head = Node(no_buku, nama_buku, harga_buku)
            self.last_node = self.head
        else:
            self.last_node.next = Node(no_buku, nama_buku, harga_buku)
            self.last_node = self.last_node.next
            self.last_node.next = self.head

    def cetak(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.no_buku, temp.nama_buku, temp.harga_buku, end="")
                print()
                temp = temp.next
                if temp == self.head:
                    break

    def editharga(self, no_buku, harga):
        current = self.head
        while current is not None:
            if current.no_buku == no_buku:
                current.harga_buku = harga
                return True
            current = current.next
        return False


def main():
    x = sllc()
    x.append(101, "\tC++\t\t", 5000)
    x.append(102, "\tJava\t", 1000)
    x.append(103, "\tPython\t", 6000)
    x.cetak()
    print()
    x.editharga(101, 2500)
    x.cetak()
    print()
    x.editharga(103, 8999)
    x.cetak()

if __name__ == "__main__":
    main()
