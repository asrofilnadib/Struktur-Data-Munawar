import random
import sys

print(sys.getrecursionlimit())


def rand(start, end, num):
    li = []
    for i in range(num):
        li.append(random.randint(start, end))
    return li


def binary(arr, L, R, x):
    sys.setrecursionlimit(1000)
    if R >= 1:
        mid = L + (R - L) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            binary(arr, mid + 1, R, x)  # kalo si x lebih kecil dari nilai mid maka ke kiri
        else:
            binary(arr, L, mid - 1, x)
    else:
        return -1


def merge(L, R):
    result = []
    i = 0
    j = 0

    while True:
        if i >= len(L):
            result.extend(R[j:])
            return result
        if j >= len(R):
            result.extend(L[i:])
            return result

        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[i])
            j += 1


def mergesort(l):
    n = len(l)
    if n <= 1:
        return  # mengindikasikan None
    mid = int(n / 2)
    Left = l[:mid]
    Right = l[mid:]
    mergesort(Left)
    mergesort(Right)
    M = merge(Left, Right)
    for i in range(n):
        l[i] = M[i]


star = 1
en = 100
nu = 12
x = rand(star, en, nu)

print("Before Sorted")
print(x)
mergesort(x)
print("\nAfter Sorted")
for i in range(len(x)):
    print("%d" % x[i], end=" ")

print("\n")
S = input("Search Indeks: ")
K = int(S)
search = binary(x, 0, len(x) - 1, K)
if search == -1:
    print("Nilai tidak ada dalam array")
else:
    print("Nilai terdapat pada array ke", search)
