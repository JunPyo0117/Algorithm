a, b = map(int, input().split())

if b >= 45:
    b = b - 45
else:
    if a == 0:
        a = 24
    b = b + 15
    a = a - 1

print(a, b)