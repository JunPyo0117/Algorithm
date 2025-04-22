n, m = map(int, input().split())

d = [i for i in range(1, n+1)]

for q in range(m):
    i, j = map(int, input().split())
    d[i-1:j] = d[i-1:j][::-1]

for i in range(n):
    print(d[i], end=" ")
