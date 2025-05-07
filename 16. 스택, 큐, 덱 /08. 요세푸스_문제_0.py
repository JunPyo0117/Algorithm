import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num_list = deque(range(1, n+1))
result = []

for _ in range(n):
    num_list.rotate(-k + 1)
    result.append(num_list.popleft())

# print(result)
print("<" + ', '.join(map(str, result)) + ">")