n, m = map(int, input().split())

d = []
for _ in range(n +1):
    d.append([0])

for _ in range(m):
    i, j, k = map(int, input().split())
    for w in range(i, j+1):
        d[w].append(k)

for q in range(1, n+1):
    print(d[q][-1], end=" ")


# N, M = map(int, input().split())
# basket = [0] * (N+1)

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for n in range(i, j+1):
#         basket[n] = k 

# for i in range(1, N+1):
#     print(basket[i], end = ' ')