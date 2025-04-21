import sys

n = int(sys.stdin.readline())

result = []

for _ in range(n):
    result.append(int(sys.stdin.readline()))

result.sort()

print('\n'.join(map(str, result)))
