import sys

n, k = map(int, sys.stdin.readline().split())

result = sorted(list(map(int, sys.stdin.readline().split())))

print(result[n-k])