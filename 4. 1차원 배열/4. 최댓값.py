# d = []
# for _ in range(9):
#     a = int(input())
#     d.append(a)


# cnt = 1

# for i in d:
#     if i != max(d):
#         cnt += 1
#     else:
#         print(max(d))
#         print(cnt)

# print(*max(zip(map(int,open(0)),range(1,10))))

def test():
    d = []
    for _ in range(9):
        a = int(input())
        d.append(a)
    print(max(d), d.index(max(d))+1, sep="\n")
    return

test()