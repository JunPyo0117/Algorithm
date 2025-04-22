n, m = map(int, input().split())

b =[]
for i in range(n+1):
    b.append(i)

temp = 0

for _ in range(m):
    i, j = map(int, input().split())
    temp = b[i]
    b[i] = b[j]
    b[j] = temp
    

for i in range(1, n+1):
    print(b[i], end=" ")