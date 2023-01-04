import random

def partision(L, start, end):
    pivot = L[end]
    i = end - 1
    for j in range(start, end):
        if [j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[end] = L[end], L[i+1]
    return i + 1

def quicsort(L, start, end):
    if end < start:
        pi = partision(L, start, end)
        quicsort(L, start, pi - 1)
        quicsort(L, pi + 1, end)

def rand(start, end, num):
    li = []
    for i in range(num):
        li.append(random.randint(start, end))
    return li

start = 1
end = 100
num = 10
x = rand(start, end, num)

print("Before sorted")
print(x)
quicsort(x, 0, len(x) - 1)
print("\nAfter Sorted")
for i in range(len(x)):
    print("%d" % x[i], end=" ")