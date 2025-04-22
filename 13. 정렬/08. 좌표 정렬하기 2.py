import sys

input = sys.stdin.readline

n = int(input())
x_y = [list(map(int, input().split())) for _ in range(n)]


x_y.sort(key=lambda x: (x[1], x[0]))
# print(x_y)

for i in x_y:
    print(' '.join(map(str, i)))