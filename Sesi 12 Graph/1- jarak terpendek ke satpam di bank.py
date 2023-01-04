from collections import deque as queue

M = 5
N = 5

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def isvalid(i, j):
    if (i < 0 or i > M - 1) or (j < 0 or j > N - 1):
        return False
    return True


def issafe(i, j, matrix, output):
    if matrix[i][j] != 'O' or output[i][j] != -1:
        return False
    return True


def finddistance(matrix):
    output = [[-1 for i in range(N)] for i in range(M)]
    q = queue()

    for i in range(M):
        for j in range(N):
            output[i][j] = -1
            if matrix[i][j] == 'G':
                pos = [i, j, 0]
                q.appendleft(pos)
                output[i][j] = 0

    while len(q) > 0:
        curr = q.pop()
        x, y, dist = curr[0], curr[1], curr[2]

        for i in range(4):
            if isvalid(x + row[i], y + col[i]) and issafe(x + row[i], y + col[i], matrix, output):
                output[x + row[i]][y + col[i]] = dist + 1
                pos = [x + row[i], y + col[i], dist + 1]
                q.appendleft(pos)

    for i in range(M):
        for j in range(N):
            if output[i][j] > 0:
                print(output[i][j], end="\t")
            else:
                print(output[i][j], end="\t")
        print()


matrix = [['O', 'O', 'O', 'O', 'G'],
          ['O', 'W', 'W', 'O', 'O'],
          ['O', 'O', 'O', 'W', 'O'],
          ['G', 'W', 'W', 'W', 'O'],
          ['O', 'O', 'O', 'O', 'G']]

finddistance(matrix)
