import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
cnt = 0

for i in a:
    if i == v:
        cnt += 1

print(cnt)

# 다른 사람 풀이이
# i=input
# i()
# print(i().split().count(i()))