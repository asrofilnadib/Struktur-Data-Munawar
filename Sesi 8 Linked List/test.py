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
        print("Pemanggilan fungsi append...")
        if self.last_node is None:
            self.head = Node(no_buku, nama_buku, harga_buku)
            self.last_node = self.head
        else:
            self.last_node.next = Node(no_buku, nama_buku, harga_buku)
            self.last_node = self.last_node.next
            self.last_node.next = self.head
        input()
        self.menu()

    def menu(self):
        import os
        os.system("CLS")
        print("Daftar Menu:")
        print("[1] Menambah data")
        print("[2] Cetak data")
        print("[3] Edit harga")
        print("[4] Keluar dari program")
        pil = input("\nPilih menu >>> ")
        self.pilihmenu(pil)


    def pilihmenu(self, p):
        if p == '1':
            self.append(no_buku='', nama_buku='', harga_buku='')
        elif p == '2':
            self.cetak()
        elif p == '3':
            self.editharga(no_buku="", harga="")
        else:
            print("Program berhenti...")

    def cetak(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.no_buku, temp.nama_buku, temp.harga_buku, end="")
                print()
                temp = temp.next
                if temp == self.head:
                    break
        input()
        self.menu()

    def editharga(self, no_buku, harga):
        current = self.head
        while current is not None:
            if current.no_buku == no_buku:
                current.harga_buku = harga
                return True
            current = current.next
        input()
        self.menu()
        return False


def main():
    x = sllc()
    x.menu()

if __name__ == "__main__":
    main()
