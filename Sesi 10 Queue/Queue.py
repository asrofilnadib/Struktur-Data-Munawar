class Antrian(object):
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c

    def enqueue(self, data):
        if self.capacity == self.rear:
            print("Antrian penuh")
        else:
            self.queue.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Antrian kosong")
        else:
            self.queue.pop(0)
            self.rear -= 1

    def display(self):
        if self.front == self.rear:
            print("Antrian kosong")

        for i in self.queue:
            print(i, "<--", end=' ')

    def qFront(self):
        if self.front == self.rear:
            print("Antrian kosong")

        print("Elemen terdepan adalah: ", self.queue[self.front])

    def average(self):
        print("Rata-rata nilai yang ada pada antrian")
        print(sum(self.queue) / len(self.queue))

    def maxvalue(self):
        print("Nilai terbesar dalam antrian")
        print(max(self.queue))

    def minvalue(self):
        print("Nilai terkecil dalam antrian")
        print(min(self.queue))

    def sum(self):
        print("Jumlah nilai antrian")
        print(sum(self.queue))


if __name__ == "__main__":
    q = Antrian(6)
    q.display()
    print()
    q.enqueue(10)
    q.enqueue(40)
    q.enqueue(55)
    q.display()
    print()
    q.dequeue()
    q.enqueue(60)
    q.enqueue(30)
    q.display()
    print()
    q.average()
    q.maxvalue()
    q.minvalue()
    q.sum()
    q.qFront()
