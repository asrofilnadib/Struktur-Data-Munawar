import random


def bubble_sort(l):
    n = len(l)
    for i in range(0, n):
        for j in range(i + 1, n):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l


def rand(start, num, end):
    li = []
    for j in range(num):
        li.append(random.randint(start, end))
    return li


star = 10
en = 200
nu = 12
l = rand(star, nu, en)

print("Before Sorted")
print(l)
bubble_sort(l)
print("\nAfter Sorted")
for i in range(len(l)):
    print("%d " % l[i], end=" ")
