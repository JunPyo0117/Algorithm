import sys
input = sys.stdin.readline

n = sorted(list(map(int, input().strip())), reverse=True)


print(''.join(map(str, n)))