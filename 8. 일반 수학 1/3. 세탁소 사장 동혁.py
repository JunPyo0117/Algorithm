t = int(input())

arry = []
for _ in range(t):
    val = int(input())
    a, b = divmod(val, 25)
    c, d = divmod(b, 10)
    e, f = divmod(d, 5)
    g, h = divmod(f, 1)
    arry.append([a,c,e,g])

for i in range(t):
    print(*arry[i])

# ======================
n = int(input())

for _ in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money//i, end=' ')
        money = money%i
    print()
