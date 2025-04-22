import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())

# print(board)
cnt = []

for i in range(n-7):
    for j in range(m-7):
        index1=0
        index2=0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        index1 += 1
                    if board[x][y] != 'B':
                        index2 += 1
                else:
                    if board[x][y] != 'B':
                        index1 += 1
                    if board[x][y] != 'W':
                        index2 += 1 
        cnt.append(min(index1, index2))
print(min(cnt))