n, x = map(int, input().split())
a = list(map(int, input().split()))

# d =''
# for i in a:
#     if i < x:
#         d += str(i) + " "

# print(d)

for i in a:
    if i < x:
        print(i, end=" ")