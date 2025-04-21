import sys

n = int(sys.stdin.readline())

result = []

for i in range(n):
    if i + sum(map(int, str(i))) == n:
        result.append(i)
 
if result == []:
    print(0)
else:
    print(min(result))
