import sys

n, m = map(int, sys.stdin.readline().split())

result = []
chk = [False] * (n+1)


def recursive(num):
    if num == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recursive(num+1)
            chk[i] = False
            result.pop()

recursive(0)