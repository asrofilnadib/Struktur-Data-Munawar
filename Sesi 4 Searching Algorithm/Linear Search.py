import random

def linear(l, x, n):
    for i in range(n):
        if l[i] == x:
            return i    # mengembalikan nilai yang ada dalam array => ketemu lah ya ini
    return -1           # keterangan -1 itu nilai yang lu cari gada di array

arr = [10, 8, 1, 90, 74, 55, 32, 86]
n = len(arr)
x = 32

result = linear(arr, x, n)
if result == -1:
    print("Nilai tidak ada dalam indeks")
else:
    print("Nilai berada pada indeks ke", result)
