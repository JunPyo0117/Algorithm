import sys

result = []

for _ in range(5):
    result.append(int(sys.stdin.readline()))

result.sort()

print(sum(result)//5, result[2], sep="\n")