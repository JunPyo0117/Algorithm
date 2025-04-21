s = int(input())

for i in range(s):
    print(" " * (s - i - 1) + "*" * (2 * i + 1))

for i in range(s - 2, -1, -1):
    print(" " * (s - i - 1) + "*" * (2 * i + 1))

# ==============================================
# n = int(input())
# for i in range(1, n):
#     print(' '*(n-i) + '*'*(2*i-1))
# for i in range(n, 0, -1):
#     print(' '*(n-i) + '*'*(2*i-1))