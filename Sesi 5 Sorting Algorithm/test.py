# Python program for implementation of Selection
# Sort
import random

def rand(start, num, end):
    li = []
    for i in range(num):
        li.append(random.randint(start, end))
    return li

star = 10
en = 100
nu = 9
x = rand(star, nu, en)

def seleksi(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


print(x)
print("Sorted array")
for i in range(len(x)):
    print("%d" % x[i], end=" ")
