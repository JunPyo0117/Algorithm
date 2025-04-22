a_list = []

for _ in range(9):
    a_list.append(list(map(int, input().split())))

max_val = []


for i in range(9):
    max_val.append(max(a_list[i]))

row = 0
col = 0

for i in range(9):
    for j in range(9):
        if a_list[i][j] == max(max_val):
            row = i
            col = j


print(max(max_val))
print(row+1, col+1)

# =====================
# max_n = 0
# for i in range(9):
#     value = list(map(int, input().split()))

#     if max(value) > max_n:
#         max_n = max(value)  # 최댓값
#         a = i + 1  # 행
#         # index함수를 쓰면 max_n 값이 있으면 max_n의 위치 값을 돌려줌
#         b = value.index(max_n) + 1

# print(max_n)
# print(a, b)