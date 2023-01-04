from typing import List


class Temple:
    def __init__(self, l: int, r: int):
        self.L = l
        self.R = r


def offeringNumber(n: int, heightTemple: List[int]) -> int:
    chainSize = [0] * n

    for i in range(n):
        chainSize[i] = Temple(-1, -1)

    chainSize[0].L = 1
    chainSize[-1].R = 1

    for i in range(1, n):
        if heightTemple[i - 1] < heightTemple[i]:
            chainSize[i].L = chainSize[i - 1].L + 1
        else:
            chainSize[i].L = 1

    for i in range(n - 2, -1, -1):
        if heightTemple[i + 1] < heightTemple[i]:
            chainSize[i].R = chainSize[i + 1].R + 1
        else:
            chainSize[i].R = 1

    sm = 0
    for i in range(n):
        sm += max(chainSize[i].L,
                  chainSize[i].R)
    return sm


if __name__ == '__main__':
    arr3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 3, 8, 5, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 6, 8, 4, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 0, 4, 7, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0],
            [0, 0, 6, 4, 0, 0, 0, 0, 0, 4, 6, 0, 0],
            [0, 0, 8, 7, 2, 5, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 4, 0, 0, 10, 0, 0, 0, 0, 3, 8, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 6, 5, 3, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 2, 0]]
    print("jarak terpendek dari titik 1 ke titik 12 adalah", offeringNumber(9, arr3))
