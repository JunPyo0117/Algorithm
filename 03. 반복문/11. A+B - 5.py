import sys

while True:
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(a+b)


# import sys

# for i in range(1, 100):
#     a,b = map(int, sys.stdin.readline().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)