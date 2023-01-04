import random

# Pengurutan Menurun
def selection_sort(X):
    global j
    n = len(X)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if X[min_idx] > X[j]:
                min_idx = j
        X[i], X[min_idx] = X[min_idx], X[i]


# # Pengurutan Menaik
# def seleksi_sort(Y):
#     global j
#     n = len(Y)
#     for i in range(n):
#         max_index = i
#         for j in range(i + 1, n):
#             if Y[j] > Y[max_index]:
#                 max_index = j
#         Y[j], Y[max_index] = Y[max_index], Y[j]
#     return Y


def rand(start, num, end):
    li = []
    for j in range(num):
        li.append(random.randint(start, end))
    return li


star = 1
nu = 10
en = 100
x = rand(star, nu, en)

print("Before Sorted")
print(x)
selection_sort(x)
print("\nAfter Sorted:")
print("A: Menurun")
for i in range(len(x)):
    print("%d" % x[i], end=" ")
#
# print("\nB: Menaik")
# seleksi_sort(l)
# for i in range(len(l)):
#     print("%d" % l[i], end=" ")
