n, m = map(int, input().split())

a_list = []
b_list = []
c_list = []

for _ in range(n):
    a_list.append(list(map(int, input().split())))


for _ in range(n):
    b_list.append(list(map(int, input().split())))


for i in range(n):
    row = []
    for j in range(m):
        row.append(a_list[i][j] + b_list[i][j])
    c_list.append(row)


for row in c_list:
    print(*row)

# print(a_list)
# print(b_list)
# print(c_list)