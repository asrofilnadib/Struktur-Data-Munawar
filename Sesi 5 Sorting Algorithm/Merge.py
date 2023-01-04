import random


def mergesort(l):
    n = len(l)
    if n <= 1:
        return
    mid = int(n / 2)  # nyari tengahnya
    # membagi elemen jadi 2 bagian
    L = l[:mid]
    R = l[mid:]
    mergesort(L)  # sorting yang kiri
    mergesort(R)  # sorting yang kanan
    M = merge(L, R)
    for i in range(n):
        l[i] = M[i]


def merge(L, R):
    result = []
    i = 0
    j = 0

    while True:
        if i >= len(L):  # Jika L udah selesai, maka tambah items dari B
            result.extend(R[j:])  # extend adalah menambah nilai ke list dari belakangnya
            return result
        if j >= len(R):  # caranya sama, cuma dibalik
            result.extend(L[i:])
            return result

        if L[i] <= R[j]:  # memasukan elemen terkecil ke dalam hasil
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1


def rand(start, num, end):
    li = []
    for j in range(num):
        li.append(random.randint(start, end))
    return li


star = 1
en = 100
nu = 12
x = rand(star, nu, en)

print("Before Sorted")
print(x)
mergesort(x)
print("\nAfter Sorted")
for i in range(len(x)):
    print("%d" % x[i], end=" ")

