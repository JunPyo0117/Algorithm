# import sys

# input = sys.stdin.readline

# n = int(input())
# result = []
# for i in range(n):
#     a, b = map(int, input().split())
#     result.append([a, b])

# result.sort()

# # print(result)

# for i in result:
#     print(' '.join(map(str, i)))

# ================================================
import sys

input = sys.stdin.readline

n = int(input())
x_y = [list(map(int, input().split())) for _ in range(n)]


x_y.sort()
# print(x_y)

for i in x_y:
    print(' '.join(map(str, i)))