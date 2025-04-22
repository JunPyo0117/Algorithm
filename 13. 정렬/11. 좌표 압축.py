import sys
# fksssdhskajfhkjas
input = sys.stdin.readline

n = int(input())

x = list(map(int, input().split()))
#[2, 4, -10, 4, -9]

set_x = list(set(x))

set_x.sort()

# print(set_x)
# [-10, -9, 2, 4]
dic = {}

for i in range(len(set_x)):
    dic[set_x[i]] = i

# print(dic)

for i in x:
    print(dic[i], end=' ')

