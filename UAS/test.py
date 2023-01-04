import sys

class Menu(object):
    def __init__(self, data=''):
        self.data = data
        self.nilai = []
        self.choice = {
            "1": self.input_data,
            "2": self.show_data,
            "3": self.quit,
        }

    def displaymenu(self):
        print("""
        Daftar Menu
        
        1. input data siswa
        2. munculin data
        3. quit
        
        """)

    def input_data(self):
        cls = int(input("masukan kelas"))
        self.siswa = str(input("masukan nama"))

        self.indo = int(input("masukan indo"))
        self.pkn = int(input("masukan pkn"))
        self.mtk = int(input("masukan mtk"))

        self.nilai.append(self.indo + self.pkn + self.mtk)

    def rerata(self):
        nilai = self.indo + self.pkn + self.mtk
        return nilai / 3

    def show_data(self, nilai=None):
        y = Menu().rerata()
        if not nilai:
            z = self.data
            for data in z:
                print("selamat kepada %s atas nilai yang "
                      "diraih dengan total nilai %d" % (self.siswa, y))
            else:
                print("tidak ada data nilai")

    def run(self):
        while True:
            self.displaymenu()
            choice = input("enter an option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("angka yang anda masukan tidak valid")

    def quit(self):
        print("Thanks for using our program today")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()