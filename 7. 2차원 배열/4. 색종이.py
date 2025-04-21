# d = [[0] * 10 for _ in range(100)]

# n = int(input())

# for _ in range(n):
#     x, y = map(int, input().split())
#     for i in range(x, x + 10):
#         for j in range(y, y + 10):
#             d[i][j] = 1


# print(d)

# =======================================================
# 100x100 크기의 빈 도화지 만들기
d = [[0] * 100 for _ in range(100)]

# 색종이 수 입력
n = int(input())

# 색종이 좌표 입력 및 색칠
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            d[i][j] = 1

# 넓이 계산
print(sum(row.count(1) for row in d))
